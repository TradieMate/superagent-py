
from importlib import metadata

try:
    __version__ = metadata.version("superagent-py")
except metadata.PackageNotFoundError:
    # Fallback version when package is not installed
    __version__ = "v0.2.40"
