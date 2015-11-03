import logging

__author__ = 'Steve'
__status__ = 'Development'
__date__ = '20151103'

# Config logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s - %(message)s')
# Use logging in module
logging.getLogger(__name__).addHandler(logging.NullHandler())