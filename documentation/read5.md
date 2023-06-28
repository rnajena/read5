Module read5.read5
==================

Functions
---------

    
`open(filepath: str) -> read5.Fast5Reader.Fast5Reader | read5.Slow5Reader.Slow5Reader | read5.Pod5Reader.Pod5Reader`
:   Autodetect file format using extension.
    Raises UnknownFormatException if format is unknown.
    
    Returns
    -------
    FileReader
        FileReader object of the detected file format