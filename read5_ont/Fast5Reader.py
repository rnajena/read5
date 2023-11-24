#!/usr/bin/env python
# author: Jannes Spangenberg
# e-mail: jannes.spangenberg@uni-jena.de
# github: https://github.com/JannesSP
# website: https://jannessp.github.io

from read5_ont.AbstractFileReader import AbstractFileReader
import h5py
import numpy as np

class Fast5Reader(AbstractFileReader):
    '''
    File reader for fast5 files

    Attributes
    ----------
    filepath : str
        Path to the ONT raw data file

    Raises
    ------
    FileNotFoundError
        If the given file does not exist.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def open(self) -> None:
        self._file = h5py.File(self._filepath, 'r')
        self._open = True
        self._reads = list(map(lambda s : s.split('read_')[-1], self._file.keys()))
        self._nreads = len(self._reads)
    
    def __getitem__(self, readid: str) -> h5py.Group:
        return self._file['read_' + readid]
    
    ### Root attribute found under file.attrs

    def getFileVersion(self) -> str:
        return self._file.attrs['file_version']

    ### Global read attributes found under file['<readid>'].attrs

    def getGlobalReadAttributes(self, readid : str) -> dict:
        '''
        Returns
        -------
        read_attributes : dict
            all attributes found under file['<readid>'].attrs
        '''
        return dict(self.__getitem__(readid).attrs)

    def getPoreType(self, readid : str) -> str:
        return self.getGlobalReadAttributes(readid)['pore_type'].decode('utf-8')
    
    def getRunID(self, readid : str) -> str:
        return self.getGlobalReadAttributes(readid)['run_id'].decode('utf-8')
    
    ### Attributes found under file['<readid>/Raw'].attrs

    def getRawAttributs(self, readid : str) -> dict:
        '''
        Returns
        -------
        attrs : dict
            Attributes that are found in file['<readid>/Raw'].attrs
        '''
        return dict(self.__getitem__(readid)['Raw'].attrs)

    def getDuration(self, readid : str) -> int:
        return self.getRawAttributs(readid)['duration']
    
    def getEndReason(self, readid : str) -> int:
        try:
            return self.getRawAttributs(readid)['end_reason']
        except:
            return 0
        
    def getMedianBefore(self, readid : str) -> float:
        return self.getRawAttributs(readid)['median_before']
    
    def getNumMinknowEvents(self, readid : str) -> int:
        '''
        Number of minknow events that the read contains.

        Returns
        -------
        num_minknow_events : int
            np.nan, if attribute not available
        '''
        try:
            return self.getRawAttributs(readid)['num_minknow_events']
        except:
            return np.nan
        
    def getNumReadsSinceMuxChange(self, readid : str) -> int:
        '''
        Number of selected reads since the last mux change on this reads channel

        Returns
        -------
        num_reads_since_mux_change : int
            np.nan, if attribute not available
        '''
        try:
            return self.getRawAttributs(readid)['num_reads_since_mux_change']
        except:
            return np.nan
        
    def getPredictedScaling(self, readid : str) -> tuple:
        '''
        Shift and Scale for predicted read scaling values (based on this read's raw signal)

        Returns
        -------
        (shift, scale) : tuple[float, float]
            (nan, nan), if attributes not available
        '''
        try:
            return (self.getRawAttributs(readid)['predicted_scaling_shift'], self.getRawAttributs(readid)['predicted_scaling_scale'])
        except:
            (np.nan, np.nan)

    def getReadNumber(self, readid : str) -> int:
        return self.getRawAttributs(readid)['read_number']
    
    def getStartMux(self, readid : str) -> int:
        '''
        Returns
        -------
        start_mux : int
        '''
        return self.getRawAttributs(readid)['start_mux']
    
    def getStartTime(self, readid : str) -> int:
        return self.getRawAttributs(readid)['start_time']
    
    def getTimeSinceMuxChange(self, readid : str) -> float:
        '''
        Time in seconds since the last mux change on this reads channel.
        
        Returns
        -------
        time : float
            in seconds
        '''
        try:
            return self.getRawAttributs(readid)['time_since_mux_change']
        except:
            return np.nan

    def getTrackedScalingScale(self, readid : str) -> float:
        '''
        Scale for tracked read scaling values (based on previous reads shift)

        Returns
        -------
        scale : float
        '''
        try:
            return self.getRawAttributs(readid)['tracked_scaling_scale']
        except:
            return np.nan
        
    def getTrackedScalingShift(self, readid : str) -> float:
        '''
        Shift for tracked read scaling values (based on previous reads shift)

        Returns
        -------
        shift : float
        '''
        try:
            return self.getRawAttributs(readid)['tracked_scaling_shift']
        except:
            return np.nan
        
    ### Attributes found under file['<readid>/channel_id']

    def getChannelIDAttributes(self, readid : str) -> dict:
        '''
        Returns a dictionary of all attributes stored under fast5['<readid>/channel_id']

        Parameter
        ---------
        readid : str

        Returns
        -------
        attributes : dict
        '''
        return dict(self.__getitem__(readid)['channel_id'].attrs)

    def getChannelNumber(self, readid : str) -> int:
        return int(self.getChannelIDAttributes(readid)['channel_number'])
    
    def getDigitisation(self, readid : str) -> int:
        return self.getChannelIDAttributes(readid)['digitisation']
    
    def getOffset(self, readid : str) -> float:
        return self.getChannelIDAttributes(readid)['offset']
    
    def getRange(self, readid : str) -> float:
        return self.getChannelIDAttributes(readid)['range']
    
    def getSamplingRate(self, readid : str) -> int:
        return self.getChannelIDAttributes(readid)['sampling_rate']
    
    def getCalibrationScale(self, readid : str) -> float:
        return self.getRange(readid) / self.getDigitisation(readid)
    
    ### Attributes found under file['<readid>/context_tags']

    def getContextTagsAttributes(self, readid : str) -> dict:
        '''
        Returns a dictionary of all attributes stored under fast5['<readid>/context_tags']

        Parameter
        ---------
        readid : str

        Returns
        -------
        attributes : dict
        '''
        return dict(self.__getitem__(readid)['context_tags'].attrs)
    
    def isBarcodingEnabled(self, readid : str) -> bool:
        return bool(int(self.getContextTagsAttributes(readid)['barcoding_enabled']))
    
    def getExperimentDurationSet(self, readid : str) -> int:
        return int(self.getContextTagsAttributes(readid)['experiment_duration_set'])
    
    def getExperimentType(self, readid : str) -> str:
        return self.getContextTagsAttributes(readid)['experiment_type'].decode('utf-8')
    
    def isLocalBasecalled(self, readid : str) -> bool:
        return bool(int(self.getContextTagsAttributes(readid)['local_basecalling']))
    
    def getPackage(self, readid : str) -> str:
        return self.getContextTagsAttributes(readid)['package'].decode('utf-8')
    
    def getPackageVersion(self, readid : str) -> str:
        return self.getContextTagsAttributes(readid)['package_version'].decode('utf-8')
    
    def getSequencingKit(self, readid : str) -> str:
        return self.getContextTagsAttributes(readid)['sequencing_kit'].decode('utf-8')
    
    ### Attributes found under file['<readid>/tracking_id']

    def getTrackingIDAttributes(self, readid : str) -> dict:
        '''
        Parameters
        ----------
        readid : str

        Returns
        -------
        tracking_id_attributes : dict
        '''
        return dict(self.__getitem__(readid)['tracking_id'].attrs)
    
    def getAsicID(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['asic_id'].decode('utf-8')
    
    def getAsicIDEeprom(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['asic_id_eeprom'].decode('utf-8')
    
    def getAsicTemp(self, readid : str) -> float:
        return float(self.getTrackingIDAttributes(readid)['asic_temp'])
    
    def getAsicVersion(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['asic_version'].decode('utf-8')
    
    def isAutoUpdated(self, readid : str) -> bool:
        return bool(int(self.getTrackingIDAttributes(readid)['auto_update']))
    
    def getAutoUpdateSource(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['auto_update_source'].decode('utf-8')
    
    def isBreamStandard(self, readid : str) -> bool:
        return bool(int(self.getTrackingIDAttributes(readid)['bream_is_standard']))
    
    def getConfigurationVersion(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['configuration_version'].decode('utf-8')
    
    def getDeviceID(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['device_id'].decode('utf-8')
    
    def getDeviceType(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['device_type'].decode('utf-8')
    
    def getDistributionStatus(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['distribution_status'].decode('utf-8')
    
    def getDistributionVersion(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['distribution_version'].decode('utf-8')
    
    def getExpScriptName(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['exp_script_name'].decode('utf-8')
    
    def getExpScriptPurpose(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['exp_script_purpose'].decode('utf-8')
    
    def getExpStartTime(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['exp_start_time'].decode('utf-8')
    
    def getFlowCellID(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['flow_cell_id'].decode('utf-8')
    
    def getFlowCellProductCode(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['flow_cell_product_code'].decode('utf-8')
    
    def getGuppyVersion(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['guppy_version'].decode('utf-8')
    
    def getHeatSinkTemp(self, readid : str) -> float:
        return float(self.getTrackingIDAttributes(readid)['heatsink_temp'])
    
    def getHostProductCode(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['host_product_code'].decode('utf-8')
    
    def getHostProductSerialNumber(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['host_product_serial_number'].decode('utf-8')
    
    def getHostname(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['hostname'].decode('utf-8')
    
    def getInstallationType(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['installation_type'].decode('utf-8')
    
    def getLocalFirmwareFile(self, readid : str) -> int:
        return int(self.getTrackingIDAttributes(readid)['local_firmware_file'])
    
    def getOperatingSystem(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['operating_system'].decode('utf-8')
    
    def getProtocolGroupID(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['protocol_group_id'].decode('utf-8')
    
    def getProtocolRunID(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['protocol_run_id'].decode('utf-8')
    
    def getProtocolStartTime(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['protocol_start_time'].decode('utf-8')
    
    def getProtocolVersion(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['protocols_version'].decode('utf-8')
    
    def getRunID(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['run_id'].decode('utf-8')
    
    def getSampleID(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['sample_id'].decode('utf-8')
    
    def getUSBConfig(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['usb_config'].decode('utf-8')
    
    def getVersion(self, readid : str) -> str:
        return self.getTrackingIDAttributes(readid)['version'].decode('utf-8')
    
    ### Calculations & signal conversions

    def getSignal(self, readid : str) -> np.ndarray:
        return self.__getitem__(readid)['Raw/Signal'][:]
    
    def getpASignal(self, readid :str) -> np.ndarray:
        return (self.getSignal(readid) + self.getOffset(readid)) * self.getCalibrationScale(readid)