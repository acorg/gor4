# Note that the version string must have the following format, otherwise it
# will not be found by the version() function in ../setup.py
__version__ = '1.0.1'

from .gor4 import GOR4

# Keep python linters quiet.
_ = GOR4
