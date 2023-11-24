#!/usr/bin/env python
# author: Jannes Spangenberg
# e-mail: jannes.spangenberg@uni-jena.de
# github: https://github.com/JannesSP
# website: https://jannessp.github.io

from abc import abstractmethod
import numpy as np
from read5.Exceptions import UnknownNormalizationMode

class AbstractFileReader():
    '''
    Abstract file reader class

    Attributes
    ----------
    filepath : str
        Path to the ONT raw data file

    Raises
    ------
    FileNotFoundError
        If the given file does not exist.
    '''

    ### abstract methods

    @abstractmethod
    def open(self) -> None:
        '''
        Opens and loads the reads of the raw ONT file.
        '''
        pass
        
    @abstractmethod
    def __getitem__(self, readid : str):
        '''
        Parameter
        ---------
        readid : str

        Returns
        -------
        read
            read dataset
        '''
        pass

    @abstractmethod
    def getAsicID(self, readid : str) -> str:
        '''
        Application Specific Integrated Circuit identifier (ASIC) of the flow cell (unique chip ID, enables tracking of batches of chips).

        Parameter
        ---------
        readid : str

        Returns
        -------
        asic_id : str
        '''
        pass

    @abstractmethod
    def getAsicIDEeprom(self, readid : str) -> str:
        '''
        ID of the ASIC's electrically erasable programmable read-only memory (EEPROM) of the flow cell
        
        Parameter
        ---------
        readid : str

        Returns
        -------
        asic_id_eeprom : str
        '''
        pass

    @abstractmethod
    def getAsicTemp(self, readid : str) -> float:
        '''
        ASIC chip temperature in degrees celsius at start of sequencing
        
        Parameter
        ---------
        readid : str

        Returns
        -------
        asic_temp : float
        '''
        pass

    @abstractmethod
    def getAsicVersion(self, readid : str) -> str:
        '''
        ASIC version

        Parameter
        ---------
        readid : str

        Returns
        -------
        asic_version : str
        '''
        pass

    @abstractmethod
    def isAutoUpdated(self, readid : str) -> bool:
        '''
        Auto update in MinKNOW

        Parameter
        ---------
        readid : str

        Returns
        -------
        status : bool
        '''
        pass

    @abstractmethod
    def getAutoUpdateSource(self, readid : str) -> str:
        '''
        URL to MinKNOW update source

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        url : str
        '''
        pass

    @abstractmethod
    def isBarcodingEnabled(self, readid : str) -> bool:
        '''
        Whether barcoding is enabled or not

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        status : bool
        '''
        pass

    @abstractmethod
    def isBreamStandard(self, readid : str) -> bool:
        '''
        Bream is a sequencing controlling software
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        status : bool
        '''
        pass

    @abstractmethod
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

    @abstractmethod
    def getChannelNumber(self, readid : str) -> int:
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
    def getConfigurationVersion(self, readid : str) -> str:
        '''
        MinKNOW configuration version including the experiment scripts

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        configuration_version : str
        '''
        pass
    
    @abstractmethod
    def getDeviceID(self, readid : str) -> str:
        '''
        MinION ID or GridION/PromethION device position ID

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        device_id : str
        '''
        pass
    
    @abstractmethod
    def getDeviceType(self, readid : str) -> str:
        '''
        Device type: MinION, PromethION or GridION

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        device_type : str
        '''
        pass

    @abstractmethod
    def getDigitisation(self, readid : str) -> int:
        '''
        Returns read calibration digitisation

        Parameter
        ---------
        readid : str

        Returns
        -------
        digitisation : float
        '''
        pass
    
    @abstractmethod
    def getDistributionStatus(self, readid : str) -> str:
        '''
        stable, dev, alpha or beta

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        distribution_status : str
        '''
        pass
    
    @abstractmethod
    def getDistributionVersion(self, readid : str) -> str:
        '''
        MinKNOW version

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        distribution_version : str
        '''
        pass

    @abstractmethod
    def getDuration(self, readid : str) -> int:
        '''
        Returns
        -------
        duration : int
            length of raw signal, number of signal samples
        '''
        pass
    
    @abstractmethod
    def getEndReason(self, readid : str) -> int:
        '''
        Available since FAST5 v2.2
        ATTENTION: End Reason encoding differs: fast5/slow5/blow5 vs pod5!

        Returns
        -------
        end_reason : int
            0 : unknown
            1 : partial
            2 : mux_change
            3 : unblock_mux_change
            4 : data_service_unblock_mux_change
            5 : signal_positive
            6 : signal_negative
        '''
        pass

    @abstractmethod
    def getExpScriptName(self, readid : str) -> str:
        '''
        Experiment name with selected kits and parameters in MinKNOW.
        Also called protocol name in pod5.

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        exp_script_name : str
        '''
        pass
    
    @abstractmethod
    def getExpScriptPurpose(self, readid : str) -> str:
        '''
        The purpose of the run: sequencing run or simulation playback

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        exp_script_purpose : str
        '''
        pass
    
    @abstractmethod
    def getExpStartTime(self, readid : str) -> str:
        '''
        Start time of the sequencing run in ISO 8601 standard

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        exp_start_time : str
        '''
        pass

    @abstractmethod
    def getExperimentDurationSet(self, readid : str) -> int:
        '''
        Experiment duration set when starting the sequencing run in minutes

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        duration : int
        '''
        pass

    @abstractmethod
    def getExperimentType(self, readid : str) -> str:
        '''
        Type of experiment, like DNA or RNA sequencing

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        experiment_type : str
        '''
        pass

    @abstractmethod
    def getFileVersion(self) -> str:
        '''
        Returns
        -------
        file_version : str
        '''
        pass

    @abstractmethod
    def getFlowCellID(self, readid : str) -> str:
        '''
        Unique flow cell ID

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        flow_cell_id : str
        '''
        pass
    
    @abstractmethod
    def getFlowCellProductCode(self, readid : str) -> str:
        '''
        Product code of the flowcell and pore type

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        production_code : str
        '''
        pass
    
    @abstractmethod
    def getGuppyVersion(self, readid : str) -> str:
        '''
        Guppy version used by MinKNOW

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        version : str
        '''
        pass
    
    @abstractmethod
    def getHeatSinkTemp(self, readid : str) -> float:
        '''
        Start temperature in degress celsius of the ASIC heat sink

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        temperature : float
        '''
        pass
    
    @abstractmethod
    def getHostProductCode(self, readid : str) -> str:
        '''
        Product code of the host computer

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        code : str
        '''
        pass
    
    @abstractmethod
    def getHostProductSerialNumber(self, readid : str) -> str:
        '''
        Serial number of the host computer

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        serial_number : str
        '''
        pass
    
    @abstractmethod
    def getHostname(self, readid : str) -> str:
        '''
        Computer on which the sequencing run is performed

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        hostname : str
        '''
        pass
    
    @abstractmethod
    def getInstallationType(self, readid : str) -> str:
        '''
        MinKNOW installation type

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        installation_type : str
        '''
        pass

    @abstractmethod
    def isLocalBasecalled(self, readid : str) -> bool:
        '''
        Type of experiment, like DNA or RNA sequencing

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        status : bool
        '''
        pass
    
    @abstractmethod
    def getLocalFirmwareFile(self, readid : str) -> int:
        '''
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        firmware_file : int
        '''
        pass
    
    @abstractmethod
    def getMedianBefore(self, readid : str) -> float:
        '''
        Estimated current median preceding the read, can be used as an estimate of the open pore current (no strand inside the pore)
        
        Returns
        -------
        median_before : float
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
    def getOperatingSystem(self, readid : str) -> str:
        '''
        Operating system of the host computer

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        os : str
        '''
        pass

    @abstractmethod
    def getPackage(self, readid : str) -> str:
        '''
        Bream package used during sequencing

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        package : str
        '''
        pass

    @abstractmethod
    def getPackageVersion(self, readid : str) -> str:
        '''
        Bream package version

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        package_version : str
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
    def getPoreType(self, readid : str) -> str:
        '''
        Parameter
        ---------
        readid : str

        Returns
        -------
        pore_type : str
            can be 'not_set'
        '''
        pass

    @abstractmethod
    def getProtocolGroupID(self, readid : str) -> str:
        '''
        Unique acquisition period ID set by the user, also called 'group id'

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        protocol_id : str
        '''
        pass
    
    @abstractmethod
    def getProtocolRunID(self, readid : str) -> str:
        '''
        Experiment run ID

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        prot_run_id : str
        '''
        pass
    
    @abstractmethod
    def getProtocolStartTime(self, readid : str) -> str:
        '''
        Data acquisition period start time

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        prot_start_time : str
        '''
        pass
    
    @abstractmethod
    def getProtocolVersion(self, readid : str) -> str:
        '''
        Protocol version (barcoding, kits, etc)

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        prot_version : str
        '''
        pass

    @abstractmethod
    def getRange(self, readid : str) -> np.ndarray:
        '''
        Returns read calibration range

        Parameter
        ---------
        readid : str

        Returns
        -------
        range : float
        '''
        pass

    @abstractmethod
    def getReadNumber(self, readid : str) -> int:
        '''
        Parameter
        ---------
        readid : str

        Returns
        -------
        read_number : int
        '''
        pass

    @abstractmethod
    def getRunID(self, readid : str) -> str:
        '''
        Parameter
        ---------
        readid : str

        Returns
        -------
        run_id : str
        '''
        pass

    @abstractmethod
    def getSamplingRate(self, readid) -> int:
        '''
        Measuring rate of the sensor during sequencing in Hz

        Parameter
        ---------
        readid : str

        Returns
        -------
        samplingRate : int
            sampling rate of the sequencing sensor used to sequence the given read
        '''
        pass
    
    @abstractmethod
    def getSampleID(self, readid : str) -> str:
        '''
        Custom user given sample ID

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        sample_id : str
        '''
        pass

    @abstractmethod
    def getSequencingKit(self, readid : str) -> str:
        '''
        Sequencing kit selected by the user

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        kit : str
        '''
        pass

    @abstractmethod
    def getSignal(self, readid : str) -> np.ndarray:
        '''
        Parameter
        ---------
        readid : str

        Returns
        -------
        signal : np.ndarray
            Raw integer signal of readid
        '''
        pass

    @abstractmethod
    def getStartTime(self, readid : str) -> int:
        '''
        Sample number of the sequencing start of the provided read.
        0 = start of sequencing
        
        Parameter
        ---------
        readid : str

        Returns
        -------
        startTime : int
            start of sequencing unconverted
        '''
        pass

    # @abstractmethod
    # def getStartMux(self, readid : str) -> int:
    #     '''
    #     Returns
    #     -------
    #     start_mux : int
    #     '''
    #     pass

    @abstractmethod
    def getUSBConfig(self, readid : str) -> str:
        '''
        Flow cell and host computer connection information

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        config : str
        '''
        pass
    
    @abstractmethod
    def getVersion(self, readid : str) -> str:
        '''
        MinKNOW version

        Parameter
        ---------
        readid : str
        
        Returns
        -------
        version : str
        '''
        pass

    ### explicit functions

    def __init__(self, filepath : str):
        self._file = None
        self._filepath : str = filepath
        self._index : int = -1
        self._nreads : int
        self._reads : list
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
        if self._open:
            self._file.close()
            self._open = False

    def isOpen(self) -> bool:
        '''
        Returns
        -------
        flag : bool
            open status of file
        '''
        return self._open

    def getReads(self) -> list:
        '''
        Returns
        -------
        reads : list
            list of read IDs within the file
        '''
        return self._reads
    
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
    
    def getStartTimeInMinutes(self, readid) -> float:
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
    
    def getFilePath(self) -> str:
        '''
        Returns
        -------
        filepath : str
        '''
        return self._filepath