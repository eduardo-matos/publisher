import sys
import logging

handler = logging.StreamHandler(sys.stdout)

logger = logging.getLogger('publisher')
logger.addHandler(handler)
logger.setLevel(logging.INFO)