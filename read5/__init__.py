from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .Reader import read
from .Fast5Reader import Fast5Reader
from .Pod5Reader import Pod5Reader
from .Slow5Reader import Slow5Reader
from . import Exceptions

__all__ = [
    "read",
    "Fast5Reader",
    "Pod5Reader",
    "Slow5Reader",
    "Exceptions"
]