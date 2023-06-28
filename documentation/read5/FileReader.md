Module read5.FileReader
=======================

Classes
-------

`FileReader(filepath: str)`
:   Abstract file reader class
    
    Attributes
    ----------
    filepath : str
        Path to the ONT raw data file

    ### Descendants

    * read5.Fast5Reader.Fast5Reader
    * read5.Pod5Reader.Pod5Reader
    * read5.Slow5Reader.Slow5Reader

    ### Methods

    `close(self) -> NoneType`
    :   Close the raw ONT file

    `getAsicID(self, readid: str) -> str`
    :   Application Specific Integrated Circuit identifier (ASIC) of the flow cell (unique chip ID, enables tracking of batches of chips).
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        asic_id : str

    `getAsicIDEeprom(self, readid: str) -> str`
    :   ID of the ASIC's electrically erasable programmable read-only memory (EEPROM) of the flow cell
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        asic_id_eeprom : str

    `getAsicTemp(self, readid: str) -> float`
    :   ASIC chip temperature in degrees celsius at start of sequencing
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        asic_temp : float

    `getAsicVersion(self, readid: str) -> str`
    :   ASIC version
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        asic_version : str

    `getAutoUpdateSource(self, readid: str) -> str`
    :   URL to MinKNOW update source
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        url : str

    `getCalibrationScale(self, readid: str) -> float`
    :   Parameter
        ---------
        readid : str
        
        Returns
        -------
        scale : float
            scale = range / digitisation

    `getChannelNumber(self, readid: str) -> int`
    :   Parameter
        ---------
        readid : str
        
        Returns
        -------
        channel : int
            Number of the channel where the read was sequenced

    `getConfigurationVersion(self, readid: str) -> str`
    :   MinKNOW configuration version including the experiment scripts
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        configuration_version : str

    `getDeviceID(self, readid: str) -> str`
    :   MinION ID or GridION/PromethION device position ID
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        device_id : str

    `getDeviceType(self, readid: str) -> str`
    :   Device type: MinION, PromethION or GridION
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        device_type : str

    `getDigitisation(self, readid: str) -> int`
    :   Returns read calibration digitisation
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        digitisation : float

    `getDistributionStatus(self, readid: str) -> str`
    :   stable, dev, alpha or beta
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        distribution_status : str

    `getDistributionVersion(self, readid: str) -> str`
    :   MinKNOW version
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        distribution_version : str

    `getDuration(self, readid: str) -> int`
    :   Returns
        -------
        duration : int
            length of raw signal, number of signal samples

    `getEndReason(self, readid: str) -> int`
    :   Available since FAST5 v2.2
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

    `getExpScriptName(self, readid: str) -> str`
    :   Experiment name with selected kits and parameters in MinKNOW.
        Also called protocol name in pod5.
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        exp_script_name : str

    `getExpScriptPurpose(self, readid: str) -> str`
    :   The purpose of the run: sequencing run or simulation playback
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        exp_script_purpose : str

    `getExpStartTime(self, readid: str) -> str`
    :   Start time of the sequencing run in ISO 8601 standard
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        exp_start_time : str

    `getExperimentDurationSet(self, readid: str) -> int`
    :   Experiment duration set when starting the sequencing run in minutes
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        duration : int

    `getExperimentType(self, readid: str) -> str`
    :   Type of experiment, like DNA or RNA sequencing
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        experiment_type : str

    `getFileVersion(self) -> str`
    :   Returns
        -------
        file_version : str

    `getFlowCellID(self, readid: str) -> str`
    :   Unique flow cell ID
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        flow_cell_id : str

    `getFlowCellProductCode(self, readid: str) -> str`
    :   Product code of the flowcell and pore type
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        production_code : str

    `getGuppyVersion(self, readid: str) -> str`
    :   Guppy version used by MinKNOW
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        version : str

    `getHeatSinkTemp(self, readid: str) -> float`
    :   Start temperature in degress celsius of the ASIC heat sink
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        temperature : float

    `getHostProductCode(self, readid: str) -> str`
    :   Product code of the host computer
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        code : str

    `getHostProductSerialNumber(self, readid: str) -> str`
    :   Serial number of the host computer
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        serial_number : str

    `getHostname(self, readid: str) -> str`
    :   Computer on which the sequencing run is performed
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        hostname : str

    `getInstallationType(self, readid: str) -> str`
    :   MinKNOW installation type
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        installation_type : str

    `getLocalFirmwareFile(self, readid: str) -> int`
    :   Parameter
        ---------
        readid : str
        
        Returns
        -------
        firmware_file : int

    `getMedianBefore(self, readid: str) -> float`
    :   Estimated current median preceding the read, can be used as an estimate of the open pore current (no strand inside the pore)
        
        Returns
        -------
        median_before : float

    `getOffset(self, readid: str) -> float`
    :   Parameter
        ---------
        readid : str
        
        Returns
        -------
        offset : float

    `getOperatingSystem(self, readid: str) -> str`
    :   Operating system of the host computer
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        os : str

    `getPackage(self, readid: str) -> str`
    :   Bream package used during sequencing
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        package : str

    `getPackageVersion(self, readid: str) -> str`
    :   Bream package version
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        package_version : str

    `getPoreType(self, readid: str) -> str`
    :   Parameter
        ---------
        readid : str
        
        Returns
        -------
        pore_type : str
            can be 'not_set'

    `getProtocolGroupID(self, readid: str) -> str`
    :   Unique acquisition period ID set by the user, also called 'group id'
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        protocol_id : str

    `getProtocolRunID(self, readid: str) -> str`
    :   Experiment run ID
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        prot_run_id : str

    `getProtocolStartTime(self, readid: str) -> str`
    :   Data acquisition period start time
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        prot_start_time : str

    `getProtocolVersion(self, readid: str) -> str`
    :   Protocol version (barcoding, kits, etc)
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        prot_version : str

    `getRange(self, readid: str) -> numpy.ndarray`
    :   Returns read calibration range
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        range : float

    `getReadNumber(self, readid: str) -> int`
    :   Parameter
        ---------
        readid : str
        
        Returns
        -------
        read_number : int

    `getReads(self) -> list`
    :   Returns
        -------
        reads : list
            list of read IDs within the file

    `getRunID(self, readid: str) -> str`
    :   Parameter
        ---------
        readid : str
        
        Returns
        -------
        run_id : str

    `getSampleID(self, readid: str) -> str`
    :   Custom user given sample ID
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        sample_id : str

    `getSamplingRate(self, readid) -> int`
    :   Measuring rate of the sensor during sequencing in Hz
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        samplingRate : int
            sampling rate of the sequencing sensor used to sequence the given read

    `getScale(self, readid: str, mode: str = 'median') -> float`
    :   Parameter
        ---------
        readid : str
        mode : str
            - 'median': using the median and mad for normalization
            - 'mean': using the mean and std for normalization
        
        Returns
        -------
        scale : float

    `getSequencingKit(self, readid: str) -> str`
    :   Sequencing kit selected by the user
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        kit : str

    `getShift(self, readid: str, mode: str = 'median') -> float`
    :   Parameter
        ---------
        readid : str
        mode : str
            - 'median': using the median and mad for normalization
            - 'mean': using the mean and std for normalization
        
        Returns
        -------
        shift : float

    `getSignal(self, readid: str) -> numpy.ndarray`
    :   Parameter
        ---------
        readid : str
        
        Returns
        -------
        signal : np.ndarray
            Raw integer signal of readid

    `getStartTime(self, readid: str) -> int`
    :   Sample number of the sequencing start of the provided read.
        0 = start of sequencing
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        startTime : int
            start of sequencing unconverted

    `getStartTimeInMinutes(self, readid) -> float`
    :   Parameter
        ---------
        readid : str
        
        Returns
        -------
        startTime : int
            start of sequencing converted to minutes after sequencing start

    `getUSBConfig(self, readid: str) -> str`
    :   Flow cell and host computer connection information
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        config : str

    `getVersion(self, readid: str) -> str`
    :   MinKNOW version
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        version : str

    `getZNormSignal(self, readid: str, mode: str = 'median') -> numpy.ndarray`
    :   Normalize the read signal of the provided read
        
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

    `getpASignal(self, readid: str) -> numpy.ndarray`
    :   Parameter
        ---------
        readid : str
        
        Returns
        -------
        pASignal : np.ndarray

    `isAutoUpdated(self, readid: str) -> bool`
    :   Auto update in MinKNOW
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        status : bool

    `isBarcodingEnabled(self, readid: str) -> bool`
    :   Whether barcoding is enabled or not
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        status : bool

    `isBreamStandard(self, readid: str) -> bool`
    :   Bream is a sequencing controlling software
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        status : bool

    `isLocalBasecalled(self, readid: str) -> bool`
    :   Type of experiment, like DNA or RNA sequencing
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        status : bool

    `isOpen(self) -> bool`
    :   Returns
        -------
        flag : bool
            open status of file

    `open(self) -> NoneType`
    :   Opens and loads the reads of the raw ONT file.