try:
  from read5._version import version as __version__
except ImportError:
  __version__ = "unknown"

from read5.Reader import read

__all__ = [
    "read"
]