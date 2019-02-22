import logging
from .client import *
import actionsportsnetwork.version

VERSION = actionsportsnetwork.version.__lib_version__

APP_VERSION = actionsportsnetwork.version.__action_app_version__

"""
Tracks with app (ios)
"""


try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

__all__ = ['client']