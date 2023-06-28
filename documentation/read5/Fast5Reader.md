Module read5.Fast5Reader
========================

Classes
-------

`Fast5Reader(*args, **kwargs)`
:   File reader for fast5 files
    
    Attributes
    ----------
    filepath : str
        Path to the ONT raw data file

    ### Ancestors (in MRO)

    * read5.FileReader.FileReader

    ### Methods

    `getChannelIDAttributes(self, readid: str) -> dict`
    :   Returns a dictionary of all attributes stored under fast5['<readid>/channel_id']
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        attributes : dict

    `getContextTagsAttributes(self, readid: str) -> dict`
    :   Returns a dictionary of all attributes stored under fast5['<readid>/context_tags']
        
        Parameter
        ---------
        readid : str
        
        Returns
        -------
        attributes : dict

    `getGlobalReadAttributes(self, readid: str) -> dict`
    :   Returns
        -------
        read_attributes : dict
            all attributes found under file['<readid>'].attrs

    `getNumMinknowEvents(self, readid: str) -> int`
    :   Number of minknow events that the read contains.
        
        Returns
        -------
        num_minknow_events : int
            np.nan, if attribute not available

    `getNumReadsSinceMuxChange(self, readid: str) -> int`
    :   Number of selected reads since the last mux change on this reads channel
        
        Returns
        -------
        num_reads_since_mux_change : int
            np.nan, if attribute not available

    `getPredictedScaling(self, readid: str) -> tuple[float, float]`
    :   Shift and Scale for predicted read scaling values (based on this read's raw signal)
        
        Returns
        -------
        (shift, scale) : tuple[float, float]
            (nan, nan), if attributes not available

    `getRawAttributs(self, readid: str) -> dict`
    :   Returns
        -------
        attrs : dict
            Attributes that are found in file['<readid>/Raw'].attrs

    `getStartMux(self, readid: str) -> int`
    :   Returns
        -------
        start_mux : int

    `getTimeSinceMuxChange(self, readid: str) -> float`
    :   Time in seconds since the last mux change on this reads channel.
        
        Returns
        -------
        time : float
            in seconds

    `getTrackedScalingScale(self, readid: str) -> float`
    :   Scale for tracked read scaling values (based on previous reads shift)
        
        Returns
        -------
        scale : float

    `getTrackedScalingShift(self, readid: str) -> float`
    :   Shift for tracked read scaling values (based on previous reads shift)
        
        Returns
        -------
        shift : float

    `getTrackingIDAttributes(self, readid: str) -> dict`
    :   Parameters
        ----------
        readid : str
        
        Returns
        -------
        tracking_id_attributes : dict