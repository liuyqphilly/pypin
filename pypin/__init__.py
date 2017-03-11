__version__ = '0.1'
__author__ = 'Ibrahim Ahmed'
__license__ = 'MIT'

from pypin.api import API
from pypin.models import Pin
from pypin.models import Board
from pypin.models import User

# Global, unauthenticated instance of API
api = API()