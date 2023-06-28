Module read5.Slow5Reader
========================

Classes
-------

`Slow5Reader(threads: int = 1, batchsize: int = 1, *args, **kwargs)`
:   File reader for slow5 or blow5 files
    
    Attributes
    ----------
    threads : int
        number of threads to use in C backend
    batchsize : int
        number of reads to fetch at a time. Higher numbers use more ram, but is more efficient with more threads.

    ### Ancestors (in MRO)

    * read5.FileReader.FileReader

    ### Methods

    `getAllHeaders(self) -> dict`
    :   Returns
        -------
        metadata : dict
            all metadata of the sequencing run stored in file.get_all_headers()

    `getFileType(self) -> str`
    :   Returns
        -------
        file_type : str

    `getStartMux(self, readid: str) -> int`
    :   Returns
        -------
        start_mux : int