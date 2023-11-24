from . import _version
__version__ = _version.get_versions()['version']

from read5.Reader import read

__all__ = [
    "read"
]