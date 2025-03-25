#!/usr/bin/env python
# author: Jannes Spangenberg
# e-mail: jannes.spangenberg@uni-jena.de
# github: https://github.com/JannesSP
# website: https://jannessp.github.io

import uuid
from read5.AbstractFileReader import AbstractFileReader
import pod5
import datetime
import numpy as np

class Pod5Reader(AbstractFileReader):
    '''
    File reader for pod5 files

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
        self._file = pod5.Reader(self._filepath)
        self._reads = self._file.read_ids
        self._nreads = self._file.num_reads
        self._open = True

    def getReads(self) -> list:
        return self._reads
        
    def __getitem__(self, readid : str):
        '''
        Returns the ReadRecord for the provided readid.
        '''
        return next(self._file.reads([readid]))
    
    def getAsicID(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['asic_id']
    
    def getAsicIDEeprom(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['asic_id_eeprom']

    def getAsicTemp(self, readid : str) -> float:
        return float(self.getTrackingIDDict(readid)['asic_temp'])

    def getAsicVersion(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['asic_version']
    
    def getAutoUpdateSource(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['auto_update_source']

    def isAutoUpdated(self, readid : str) -> bool:
        return bool(int(self.getTrackingIDDict(readid)['auto_update']))    

    def isBarcodingEnabled(self, readid : str) -> bool:
        return bool(int(self.getContextTagsDict(readid)['barcoding_enabled']))
    
    def isBreamStandard(self, readid : str) -> bool:
        return bool(int(self.getTrackingIDDict(readid)['bream_is_standard']))

    def getCalibration(self, readid : str) -> float:
        return self.__getitem__(readid).calibration

    def getCalibrationScale(self, readid : str) -> float:
        return self.getCalibration(readid).scale

    def getChannelNumber(self, readid : str) -> int:
        return self.getPoreObject(readid).channel

    def getConfigurationVersion(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['configuration_version']

    def getContextTagsDict(self, readid : str) -> dict:
        '''
        Returns
        -------
        context_tags : dict
        '''
        return self.getRunInfoObject(readid).context_tags

    def getDeviceID(self, readid : str) -> str:
        return self.getRunInfoObject(readid).sequencer_position
    
    def getDeviceType(self, readid : str) -> str:
        return self.getRunInfoObject(readid).sequencer_position_type

    def getDigitisation(self, readid : str) -> int:
        return self.__getitem__(readid).calibration_digitisation
    
    def getDistributionStatus(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['distribution_status']
    
    def getDistributionVersion(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['distribution_version']
    
    def getDuration(self, readid : str) -> int:
        return self.__getitem__(readid).num_samples

    def getEndReason(self, readid: str) -> int:
        '''
        ATTENTION: End Reason encoding differs: fast5/slow5/blow5 vs pod5!

        Returns
        -------
        end_reason : int
            0 : unknown
            1 : mux_change
            2 : unblock_mux_change
            3 : data_service_unblock_mux_change
            4 : signal_positive
            5 : signal_negative
        '''
        return self.__getitem__(readid).end_reason_index
    
    def getEndReasonObject(self, readid: str) -> pod5.pod5_types.EndReason:
        '''
        Returns
        -------
        end_reason : pod5.pod5_types.EndReason
        '''
        return self.__getitem__(readid).end_reason

    def getExperimentDurationSet(self, readid : str) -> int:
        return int(self.getContextTagsDict(readid)['experiment_duration_set'])

    def getExperimentType(self, readid : str) -> str:
        return self.getContextTagsDict(readid)['experiment_type']
    
    def getExpScriptPurpose(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['exp_script_purpose']

    def getExpScriptName(self, readid : str) -> str:
        return self.getRunInfoObject(readid).protocol_name

    def getExpStartTime(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['exp_start_time']

    def getFileID(self) -> uuid.UUID:
        return self._file.file_identifier
    
    # file_version : packagin.version.Version
    # contains more (& detailed) information if needed in the future
    def getFileVersion(self) -> str:
        return str(self._file.file_version)
    
    def getLocalFirmwareFile(self, readid : str) -> int:
        return int(self.getTrackingIDDict(readid)['local_firmware_file'])

    def getFlowCellID(self, readid : str) -> str:
        return self.getRunInfoObject(readid).flow_cell_id
    
    def getFlowCellProductCode(self, readid : str) -> str:
        return self.getRunInfoObject(readid).flow_cell_product_code
    
    def getGuppyVersion(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['guppy_version']

    def getHeatSinkTemp(self, readid : str) -> float:
        return float(self.getTrackingIDDict(readid)['heatsink_temp'])

    def getHostname(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['hostname']
    
    def getHostProductCode(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['host_product_code']
    
    def getHostProductSerialNumber(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['host_product_serial_number']
    
    def getInstallationType(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['installation_type']

    def isLocalBasecalled(self, readid : str) -> bool:
        return bool(int(self.getContextTagsDict(readid)['local_basecalling']))

    def getMedianBefore(self, readid : str) -> float:
        return self.__getitem__(readid).median_before

    def getNumMinknowEvents(self, readid : str) -> int:
        '''
        Number of minknow events that the read contains.

        Returns
        -------
        num_minknow_events : int
            np.nan, if attribute not available
        '''
        return self.__getitem__(readid).num_minknow_events

    def getNumReadsSinceMuxChange(self, readid : str) -> int:
        '''
        Number of selected reads since the last mux change on this reads channel

        Returns
        -------
        num_reads_since_mux_change : int
        '''
        return self.__getitem__(readid).num_reads_since_mux_change

    def getTimeSinceMuxChange(self, readid : str) -> float:
        '''
        Returns
        -------
        time_since_mux_change : float
        '''
        return self.__getitem__(readid).time_since_mux_change
    
    def getOffset(self, readid : str) -> float:
        return self.getCalibration(readid).offset
    
    def getOperatingSystem(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['operating_system']

    def getPackage(self, readid : str) -> str:
        return self.getContextTagsDict(readid)['package']
    
    def getPackageVersion(self, readid : str) -> str:
        return self.getContextTagsDict(readid)['package_version']
    
    def getProtocolGroupID(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['protocol_group_id']

    def getProtocolStartTime(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['protocol_start_time']

    def getProtocolStartTime_fromRunInfo(self, readid : str) -> str:
        return self.getRunInfoObject(readid).protocol_start_time.isoformat()

    # TODO the following function works and is correct, but the converted time seems to be wrong -> error in pod5 converter?
    def getProtocolStartTime_datetime(self, readid : str) -> datetime.datetime:
        '''
        Parameters
        ----------
        readid : str

        Returns
        -------
        protocol_start_time : datetime.datetime
        '''
        return self.getRunInfoObject(readid).protocol_start_time

    def getProtocolRunID(self, readid : str) -> str:
        return self.getRunInfoObject(readid).protocol_run_id

    def getProtocolVersion(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['protocols_version']

    def getpASignal(self, readid : str) -> np.ndarray:
        return self.__getitem__(readid).signal_pa

    def getPoreObject(self, readid : str) -> pod5.pod5_types.Pore:
        '''
        Returns
        -------
        pore : pod5.pod5_types.Pore
        '''
        return self.__getitem__(readid).pore
    
    def getPoreType(self, readid : str) -> str:
        return self.getPoreObject(readid).pore_type
    
    def getPredictedScaling(self, readid : str) -> tuple:
        '''
        Shift and Scale for predicted read scaling values (based on this read's raw signal)

        Returns
        -------
        (shift, scale) : tuple[float, float]
            (nan, nan), if attributes not available
        '''
        ShScPair = self.__getitem__(readid).predicted_scaling
        return (ShScPair.shift, ShScPair.scale)

    def getRange(self, readid : str) -> float:
        return self.__getitem__(readid).calibration_range

    def getReadNumber(self, readid : str) -> int:
        return self.__getitem__(readid).read_number

    def getRunID(self, readid : str) -> str:
        return self.getRunInfoObject(readid).acquisition_id

    def getReadObject(self, readid : str) -> pod5.pod5_types.Read:
        return self.__getitem__(readid).to_read()

    def getRunInfoObject(self, readid : str) -> pod5.pod5_types.RunInfo:
        '''
        Returns
        -------
        run_info : pod5.pod5_types.RunInfo
        '''
        return self.__getitem__(readid).run_info

    def getSampleID(self, readid : str) -> str:
        return self.getRunInfoObject(readid).sample_id

    def getSamplingRate(self, readid : str) -> int:
        return self.getRunInfoObject(readid).sample_rate
    
    def getSequencingKit(self, readid : str) -> str:
        return self.getRunInfoObject(readid).sequencing_kit

    def getSignal(self, readid : str) -> np.ndarray:
        return self.__getitem__(readid).signal

    def getStartTime(self, readid : str) -> int:
        return self.__getitem__(readid).start_sample
    
    def getTrackingIDDict(self, readid : str) -> dict:
        '''
        Returns
        -------
        tracking_id : dict
        '''
        return self.getRunInfoObject(readid).tracking_id

    def isVBZCompressed(self) -> bool:
        '''
        Returns
        -------
        flag : bool
            if file is VBZ compressed or not
        '''
        return self._file.is_vbz_compressed
    
    def getVersion(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['version']

    def getWellNumber(self, readid : str) -> int:
        '''
        Returns
        -------
        well : int
            Number of the well in the channel used for sequencing
        '''
        return self.getPoreObject(readid).well
    
    def getUSBConfig(self, readid : str) -> str:
        return self.getTrackingIDDict(readid)['usb_config']