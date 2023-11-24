#!/usr/bin/env python
# author: Jannes Spangenberg
# e-mail: jannes.spangenberg@uni-jena.de
# github: https://github.com/JannesSP
# website: https://jannessp.github.io

class UnknownFileFormatException(Exception):
    '''
    Exception raised for unknown file formats in the FileHandler.

    Attributes
    ----------
    message : str
        explanation of the error
    '''
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class UnknownNormalizationMode(Exception):
    '''
    Exception raised for unknown normalization mode during read signal normalization.

    Attributes
    ----------
    message : str
        explanation of the error
    '''
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)