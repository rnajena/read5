#!/usr/bin/env python
# author: Jannes Spangenberg
# e-mail: jannes.spangenberg@uni-jena.de
# github: https://github.com/JannesSP
# website: https://jannessp.github.io

from read5.FileReader import *
import h5py as h5

class Fast5Reader(FileReader):
    '''
    File reader for fast5 files

    Attributes
    ----------
    filepath : str
        Path to the ONT raw data file
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def open(self) -> None:
        self._file = h5.File(self._filepath, 'r')
        self._opened = True
        self._reads = list(self._file.keys())
        self._nreads = len(self._reads)
    
    def __getitem__(self, readid: str) -> h5.Group:
        return self._file[readid]
        
    def getOffset(self, readid : str) -> np.ndarray:
        return self.__getitem__(readid)['channel_id'].attrs['offset']

    def getRange(self, readid : str) -> np.ndarray:
        '''
        Parameter
        ---------
        readid : str

        Returns
        -------
        range : float
        '''
        return self.__getitem__(readid)['channel_id'].attrs['range']

    def getDigitisation(self, readid : str) -> np.ndarray:
        '''
        Parameter
        ---------
        readid : str

        Returns
        -------
        digitisation : float
        '''
        return self.__getitem__(readid)['channel_id'].attrs['digitisation']

    def getCalibrationScale(self, readid : str) -> float:
        return self.getRange(readid) / self.getDigitisation(readid)

    def getSignal(self, readid : str) -> np.ndarray:
        return self.__getitem__(readid)['Raw/Signal'][:]
    
    def getpASignal(self, readid :str) -> np.ndarray:
        return (self.getSignal(readid) + self.getOffset(readid)) * self.getCalibrationScale(readid)
    
    def getChannel(self, readid : str) -> int:
        return int(self.__getitem__(readid)['channel_id'].attrs['channel_number'])
    
    def getStartTime(self, readid : str) -> int:
        return self.__getitem__(readid)['Raw'].attrs['start_time']
    
    def getSamplingRate(self, readid : str) -> int:
        return self.__getitem__(readid)['channel_id'].attrs['sampling_rate']