Module read5.Pod5Reader
=======================

Classes
-------

`Pod5Reader(*args, **kwargs)`
:   File reader for pod5 files

    ### Ancestors (in MRO)

    * read5.FileReader.FileReader

    ### Methods

    `getCalibration(self, readid: str) -> float`
    :

    `getContextTagsDict(self, readid: str) -> dict`
    :   Returns
        -------
        context_tags : dict

    `getEndReason(self, readid: str) -> int`
    :   ATTENTION: End Reason encoding differs: fast5/slow5/blow5 vs pod5!
        
        Returns
        -------
        end_reason : int
            0 : unknown
            1 : mux_change
            2 : unblock_mux_change
            3 : data_service_unblock_mux_change
            4 : signal_positive
            5 : signal_negative

    `getEndReasonObject(self, readid: str) -> pod5.pod5_types.EndReason`
    :   Returns
        -------
        end_reason : pod5.pod5_types.EndReason

    `getFileID(self) -> uuid.UUID`
    :

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

    `getPoreObject(self, readid: str) -> pod5.pod5_types.Pore`
    :   Returns
        -------
        pore : pod5.pod5_types.Pore

    `getPredictedScaling(self, readid: str) -> tuple[float, float]`
    :   Shift and Scale for predicted read scaling values (based on this read's raw signal)
        
        Returns
        -------
        (shift, scale) : tuple[float, float]
            (nan, nan), if attributes not available

    `getProtocolStartTime_datetime(self, readid: str) -> datetime.datetime`
    :   Parameters
        ----------
        readid : str
        
        Returns
        -------
        protocol_start_time : datetime.datetime

    `getProtocolStartTime_fromRunInfo(self, readid: str) -> str`
    :

    `getReadObject(self, readid: str) -> pod5.pod5_types.Read`
    :

    `getRunInfoObject(self, readid: str) -> pod5.pod5_types.RunInfo`
    :   Returns
        -------
        run_info : pod5.pod5_types.RunInfo

    `getTimeSinceMuxChange(self, readid: str) -> float`
    :   Returns
        -------
        time_since_mux_change : float

    `getTrackingIDDict(self, readid: str) -> dict`
    :   Returns
        -------
        tracking_id : dict

    `getWellNumber(self, readid: str) -> int`
    :   Returns
        -------
        well : int
            Number of the well in the channel used for sequencing

    `isVBZCompressed(self) -> bool`
    :   Returns
        -------
        flag : bool
            if file is VBZ compressed or not