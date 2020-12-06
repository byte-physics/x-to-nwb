"""
This package allows to create NeuroDataWithoutBorders v2 files from ABF and DAT files.

See Readme.md for more information.
"""

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

from .conversion import convert_cli
