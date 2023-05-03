#!/usr/bin/env python
# author: Jannes Spangenberg
# e-mail: jannes.spangenberg@uni-jena.de
# github: https://github.com/JannesSP
# website: https://jannessp.github.io

from read5.FileReader import *
import pod5 as p5

class Pod5Reader(FileReader):
    '''
    File reader for pod5 files
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def open(self) -> None:
        self._file = p5.Reader(self._filepath)
        self._reads = self._file.read_ids
        self._nreads = self._file.num_reads
        self._opened = True

    def getReads(self) -> list:
        return self._reads
        
    def __getitem__(self, readid : str):
        '''
        Returns the ReadRecord for the provided readid.
        '''
        return next(self._file.reads([readid]))
    
    def getSignal(self, readid : str) -> np.ndarray:
        return self.__getitem__(readid).signal

    def getCalibration(self, readid : str):
        return self.__getitem__(readid).calibration

    def getOffset(self, readid : str) -> float:
        return self.getCalibration(readid).offset

    def getCalibrationScale(self, readid : str) -> float:
        return self.getCalibration(readid).scale

    def getpASignal(self, readid : str) -> np.ndarray:
        return self.__getitem__(readid).signal_pa

    def getPore(self, readid : str):
        return self.__getitem__(readid).pore

    def getChannel(self, readid : str) -> int:
        return self.getPore(readid).channel

    def getRunInfo(self, readid : str):
        return self.__getitem__(readid).run_info

    def getStartTime(self, readid : str) -> int:
        return self.__getitem__(readid).start_sample

    def getSamplingRate(self, readid : str) -> int:
        return self.getRunInfo(readid).sample_rate