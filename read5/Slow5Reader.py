#!/usr/bin/env python
# author: Jannes Spangenberg
# e-mail: jannes.spangenberg@uni-jena.de
# github: https://github.com/JannesSP
# website: https://jannessp.github.io

from read5.AbstractFileReader import AbstractFileReader
import pyslow5
import numpy as np

class Slow5Reader(AbstractFileReader):
    '''
    File reader for slow5 or blow5 files

    Attributes
    ----------
    threads : int
        number of threads to use in C backend
    batchsize : int
        number of reads to fetch at a time. Higher numbers use more ram, but is more efficient with more threads.
    filepath : str
        Path to the ONT raw data file

    Raises
    ------
    FileNotFoundError
        If the given file does not exist.
    '''
    def __init__(self, threads : int = 1, batchsize : int = 1, *args, **kwargs):
        self._threads = threads
        self._batchsize = batchsize
        super().__init__(*args, **kwargs)
    
    def open(self) -> None:
        self._file = pyslow5.Open(self._filepath, 'r')
        if self._threads > 1:
            self._reads = self._file.seq_reads_multi(threads=self._threads, batchsize=self._batchsize)
        else:
            self._reads, self._nreads = self._file.get_read_ids()
        self._open = True
        
    def __getitem__(self, readid : str):
        return self._file.get_read(readid)

    def getSignal(self, readid : str) -> np.ndarray:
        return self.__getitem__(readid)['signal']

    def getOffset(self, readid : str) -> float:
        return self.__getitem__(readid)['offset']

    def getRange(self, readid : str) -> float:
        return self.__getitem__(readid)['range']

    def getDigitisation(self, readid : str) -> int:
        return self.__getitem__(readid)['digitisation']
    
    def getCalibrationScale(self, readid : str) -> float:
        return self.getRange(readid) / self.getDigitisation(readid)

    def getpASignal(self, readid :str) -> np.ndarray:
        return self._file.get_read(readid, pA=True)['signal']

    def getChannelNumber(self, readid : str) -> int:
        return int(self._file.get_read(readid, aux='channel_number')['channel_number'])

    def getStartTime(self, readid : str) -> int:
        return self._file.get_read(readid, aux='start_time')['start_time']
    
    def getReadNumber(self, readid : str) -> int:
        return self._file.get_read(readid, aux='read_number')['read_number']
    
    def getMedianBefore(self, readid : str) -> int:
        return self._file.get_read(readid, aux='median_before')['median_before']
    
    def getStartMux(self, readid : str) -> int:
        '''
        Returns
        -------
        start_mux : int
        '''
        return self._file.get_read(readid, aux='start_mux')['start_mux']
    
    def getEndReason(self, readid : str) -> int:
        return self._file.get_read(readid, aux='end_reason')['end_reason']

    def getDuration(self, readid : str) -> int:
        return self.__getitem__(readid)['len_raw_signal']

    def getSamplingRate(self, readid : str) -> int:
        return self.__getitem__(readid)['sampling_rate']

    ### get_all_headers

    def getAllHeaders(self) -> dict:
        '''
        Returns
        -------
        metadata : dict
            all metadata of the sequencing run stored in file.get_all_headers()
        '''
        return self._file.get_all_headers()
    
    def getAsicID(self, readid : str = None) -> str:
        return self.getAllHeaders()['asic_id']
    
    def getAsicIDEeprom(self, readid : str = None) -> str:
        return self.getAllHeaders()['asic_id_eeprom']
    
    def getAsicTemp(self, readid : str = None) -> float:
        return float(self.getAllHeaders()['asic_temp'])
    
    def getAsicVersion(self, readid : str = None) -> str:
        return self.getAllHeaders()['asic_version']
    
    def isAutoUpdated(self, readid : str = None) -> bool:
        return bool(int(self.getAllHeaders()['auto_update']))
        
    def getAutoUpdateSource(self, readid : str = None) -> str:
        return self.getAllHeaders()['auto_update_source']
    
    def isBarcodingEnabled(self, readid : str = None) -> bool:
        return bool(int(self.getAllHeaders()['barcoding_enabled']))
    
    def isBreamStandard(self, readid : str = None) -> bool:
        return bool(int(self.getAllHeaders()['bream_is_standard']))

    def getConfigurationVersion(self, readid : str = None) -> str:
        return self.getAllHeaders()['configuration_version']
    
    def getDeviceID(self, readid : str = None) -> str:
        return self.getAllHeaders()['device_id']

    def getDeviceType(self, readid : str = None) -> str:
        return self.getAllHeaders()['device_type']

    def getDistributionStatus(self, readid : str = None) -> str:
        return self.getAllHeaders()['distribution_status']

    def getDistributionVersion(self, readid : str = None) -> str:
        return self.getAllHeaders()['distribution_version']

    def getExpScriptName(self, readid : str = None) -> str:
        return self.getAllHeaders()['exp_script_name']

    def getExpScriptPurpose(self, readid : str = None) -> str:
        return self.getAllHeaders()['exp_script_purpose']

    def getExpStartTime(self, readid : str = None) -> str:
        return self.getAllHeaders()['exp_start_time']
    
    def getExperimentDurationSet(self, readid : str = None) -> int:
        return int(self.getAllHeaders()['experiment_duration_set'])
    
    def getExperimentType(self, readid : str = None) -> str:
        return self.getAllHeaders()['experiment_type']
    
    def getFileType(self) -> str:
        '''
        Returns
        -------
        file_type : str
        '''
        return self.getAllHeaders()['file_type']

    def getFileVersion(self) -> str:
        return self.getAllHeaders()['file_version']

    def getFlowCellID(self, readid : str = None) -> str:
        return self.getAllHeaders()['flow_cell_id']
    
    def getFlowCellProductCode(self, readid :  str = None) -> str:
        return self.getAllHeaders()['flow_cell_product_code']
    
    def getGuppyVersion(self, readid : str = None) -> str:
        return self.getAllHeaders()['guppy_version']

    def getHeatSinkTemp(self, readid : str = None) -> float:
        return float(self.getAllHeaders()['heatsink_temp'])
    
    def getHostProductCode(self, readid : str = None) -> str:
        return self.getAllHeaders()['host_product_code']
    
    def getHostProductSerialNumber(self, readid : str = None) -> str:
        return '' if self.getAllHeaders()['host_product_serial_number'] is None else self.getAllHeaders()['host_product_serial_number']
    
    def getHostname(self, readid : str = None) -> str:
        return self.getAllHeaders()['hostname']
    
    def getInstallationType(self, readid : str = None) -> str:
        return self.getAllHeaders()['installation_type']
    
    def isLocalBasecalled(self, readid : str = None) -> bool:
        return bool(int(self.getAllHeaders()['local_basecalling']))
    
    def getLocalFirmwareFile(self, readid : str = None) -> int:
        return int(self.getAllHeaders()['local_firmware_file'])
    
    def getOperatingSystem(self, readid : str = None) -> str:
        return self.getAllHeaders()['operating_system']
    
    def getPackage(self, readid : str = None) -> str:
        return self.getAllHeaders()['package']
    
    def getPackageVersion(self, readid : str = None) -> str:
        return self.getAllHeaders()['package_version']
    
    def getPoreType(self, readid : str = None) -> str:
        return self.getAllHeaders()['pore_type']
    
    def getProtocolGroupID(self, readid : str = None) -> str:
        return self.getAllHeaders()['protocol_group_id']

    def getProtocolRunID(self, readid : str = None) -> str:
        return self.getAllHeaders()['protocol_run_id']

    def getProtocolStartTime(self, readid : str = None) -> str:
        return self.getAllHeaders()['protocol_start_time']
    
    def getProtocolVersion(self, readid : str = None) -> str:
        return self.getAllHeaders()['protocols_version']
    
    def getRunID(self, readid : str = None) -> str:
        return self.getAllHeaders()['run_id']

    def getSampleID(self, readid : str = None) -> str:
        return self.getAllHeaders()['sample_id']

    def getSequencingKit(self, readid : str = None) -> str:
        return self.getAllHeaders()['sequencing_kit']

    def getUSBConfig(self, readid : str = None) -> str:
        return self.getAllHeaders()['usb_config']
    
    def getVersion(self, readid : str = None) -> str:
        return self.getAllHeaders()['version']