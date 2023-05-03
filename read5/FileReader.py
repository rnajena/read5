#!/usr/bin/env python
# author: Jannes Spangenberg
# e-mail: jannes.spangenberg@uni-jena.de
# github: https://github.com/JannesSP
# website: https://jannessp.github.io

from abc import abstractmethod
import numpy as np

from read5.Exceptions import UnknownNormalizationMode

class FileReader():
    '''
    Abstract file reader class

    Attributes
    ----------
    filepath : str
        Path to the ONT raw data file
    '''

    @abstractmethod
    def open(self) -> None:
        '''
        Opens and loads the reads of the raw ONT file.
        '''
        pass
        
    @abstractmethod
    def __getitem__(self, readid : str):
        '''
        Returns
        -------
        read
            read dataset
        '''
        pass

    @abstractmethod
    def getSignal(self, readid : str) -> np.ndarray:
        '''
        Returns
        -------
        signal : np.ndarray
            Raw integer signal of readid
        '''
        pass

    @abstractmethod
    def getOffset(self, readid : str) -> float:
        '''
        Parameter
        ---------
        readid : str

        Returns
        -------
        offset : float
        '''
        pass

    @abstractmethod
    def getpASignal(self, readid :str) -> np.ndarray:
        '''
        Parameter
        ---------
        readid : str

        Returns
        -------
        pASignal : np.ndarray
        '''
        pass

    @abstractmethod
    def getChannel(self, readid : str) -> int:
        '''
        Parameter
        ---------
        readid : str

        Returns
        -------
        channel : int
            Number of the channel where the read was sequenced
        '''
        pass

    @abstractmethod
    def getStartTime(self, readid : str) -> int:
        '''
        Parameter
        ---------
        readid : str

        Returns
        -------
        startTime : int
            start of sequencing unconverted
        '''
        pass

    @abstractmethod
    def getSamplingRate(self, readid : str) -> int:
        '''
        Parameter
        ---------
        readid : str

        Returns
        -------
        samplingRate : float
            sampling rate of the sequencing sensor used to sequence the given read
        '''
        pass

    def __init__(self, filepath : str):
        self._filepath = filepath
        self._file = None
        self._index = -1
        self.open()

    def __iter__(self):
        return self
    
    def __len__(self) -> int:
        '''
        Returns
        -------
        length : int
            number of reads in the file
        '''
        return self._nreads
    
    def __next__(self):
        self._index += 1
        if self._index >= self._nreads:
            raise StopIteration
        else:
            return self._reads[self._index]
    
    def close(self) -> None:
        '''
        Close the raw ONT file
        '''
        if self._opened:
            self._file.close()
            self._opened = False

    def isOpen(self) -> bool:
        '''
        Returns
        -------
        flag : bool
            open status of file
        '''
        return self._opened

    def getReads(self) -> list:
        '''
        Returns
        -------
        reads : list
            list of read IDs within the file
        '''
        return self._reads
    
    def getCalibrationScale(self, readid : str) -> float:
        '''
        Parameter
        ---------
        readid : str

        Returns
        -------
        scale : float
            scale = range / digitisation
        '''
        pass
    
    def getShift(self, readid : str, mode : str = 'median') -> float:
        '''
        Parameter
        ---------
        readid : str
        mode : str
            - 'median': using the median and mad for normalization
            - 'mean': using the mean and std for normalization

        Returns
        -------
        shift : float
        '''
        if mode == 'median':
            return np.median(self.getpASignal(readid))
        elif mode == 'mean':
            return np.mean(self.getpASignal(readid))
        else:
            raise UnknownNormalizationMode

    def getScale(self, readid : str, mode : str = 'median') -> float:
        '''
        Parameter
        ---------
        readid : str
        mode : str
            - 'median': using the median and mad for normalization
            - 'mean': using the mean and std for normalization

        Returns
        -------
        scale : float
        '''
        if mode == 'median':
            return 1.4826 * np.median(np.abs(self.getpASignal(readid) - self.getShift(readid, mode)))
        elif mode == 'mean':
            return np.std(self.getpASignal(readid))
        else:
            raise UnknownNormalizationMode
        
    def getZNormSignal(self, readid : str, mode : str = 'median') -> np.ndarray:
        '''
        Normalize the read signal of the provided read

        Parameter
        ---------
        readid : str
        mode : str
            - 'median': using the median and mad for normalization
            - 'mean': using the mean and std for normalization

        Returns
        -------
        normSignal : np.ndarray
            Z normalized read signal
        '''
        return (self.getpASignal(readid) - self.getShift(readid, mode)) / self.getScale(readid, mode)
    
    def getStartTimeInMinutes(self, readid : str) -> float:
        '''
        Parameter
        ---------
        readid : str

        Returns
        -------
        startTime : int
            start of sequencing converted to minutes after sequencing start
        '''
        return self.getStartTime(readid) / self.getSamplingRate(readid) / 60