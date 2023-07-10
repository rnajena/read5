from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from . import Reader
from . import Fast5Reader
from . import Pod5Reader
from . import Slow5Reader
from . import Exceptions
from . import AbstractFileReader

__all__ = ["Reader", "Fast5Reader", "Pod5Reader", "Slow5Reader", "Exceptions", "AbstractFileReader"]