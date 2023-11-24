from . import _version
__version__ = _version.get_versions()['version']

from read5_ont.Reader import read

__all__ = [
    "read"
]