#!/usr/bin/env python
# author: Jannes Spangenberg
# e-mail: jannes.spangenberg@uni-jena.de
# github: https://github.com/JannesSP
# website: https://jannessp.github.io

from read5_ont.Exceptions import UnknownFileFormatException
from read5_ont.Fast5Reader import Fast5Reader
from read5_ont.Pod5Reader import Pod5Reader

def read(filepath : str):
    '''
    Autodetect file format using extension.
    Raises UnknownFormatException if format is unknown.

    Returns
    -------
    FileReader
        FileReader object of the detected file format
    '''
    if filepath.lower().endswith('.fast5'):
        return Fast5Reader(filepath)
    elif filepath.lower().endswith('.pod5'):
        return Pod5Reader(filepath)
    else:
        raise UnknownFileFormatException(f'Unknown file format: {filepath.split(".")[-1]}')
