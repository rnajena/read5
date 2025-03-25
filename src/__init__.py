try:
  from src._version import version as __version__
except ImportError:
  __version__ = "unknown"

from src.Reader import read

__all__ = [
    "read"
]