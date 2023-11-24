from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from read5.Reader import read

__all__ = [
    "read"
]