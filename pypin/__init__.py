__version__ = '0.1'
__author__ = 'Ibrahim Ahmed'
__license__ = 'MIT'

from pypin.api import API
import pypin.exceptions as exceptions

# Global, unauthenticated instance of API
api = API()