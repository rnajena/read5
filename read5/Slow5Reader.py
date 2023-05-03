#!/usr/bin/env python
# author: Jannes Spangenberg
# e-mail: jannes.spangenberg@uni-jena.de
# github: https://github.com/JannesSP
# website: https://jannessp.github.io

from read5.FileReader import *
import pyslow5 as ps5

class Slow5Reader(FileReader):
    '''
    File reader for slow5 or blow5 files

    Attributes
    ----------
    threads : int
        number of threads to use in C backend
    batchsize : int
        number of reads to fetch at a time. Higher numbers use more ram, but is more efficient with more threads.
    '''
    def __init__(self, threads : int = 1, batchsize : int = 1, *args, **kwargs):
        self._threads = threads
        self._batchsize = batchsize
        super().__init__(*args, **kwargs)
    
    def open(self) -> None:
        self._file = ps5.Open(self._filepath, 'r')
        if self._threads > 1:
            self._reads = self._file.seq_reads_multi(threads=self._threads, batchsize=self._batchsize)
        else:
            self._reads, self._nreads = self._file.get_read_ids()
        self._opened = True
        
    def __getitem__(self, readid : str):
        return self._file.get_read(readid)

    def getSignal(self, readid : str) -> np.ndarray:
        return self.__getitem__(readid)['signal']

    def getOffset(self, readid : str) -> float:
        return self.__getitem__(readid)['offset']

    def getRange(self, readid : str) -> float:
        '''
        Parameter
        ---------
        readid : str

        Returns
        -------
        range : float
        '''
        return self.__getitem__(readid)['range']

    def getDigitisation(self, readid : str) -> float:
        '''
        Parameter
        ---------
        readid : str

        Returns
        -------
        digitisation : float
        '''
        return self.__getitem__(readid)['digitisation']
    
    def getCalibrationScale(self, readid : str) -> float:
        return self.getRange(readid) / self.getDigitisation(readid)

    def getpASignal(self, readid :str) -> np.ndarray:
        return self._file.get_read(readid, pA=True)['signal']

    def getChannel(self, readid : str) -> int:
        return int(self._file.get_read(readid, aux='channel_number')['channel_number'])

    def getStartTime(self, readid: str) -> int:
        return self._file.get_read(readid, aux='start_time')['start_time']

    def getSamplingRate(self, readid : str) -> int:
        return self.__getitem__(readid)['sampling_rate']