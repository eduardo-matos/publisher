from random import randint
from publisher import config

def sample_amount():
  return randint(
    config.MEAN_MSG_COUNT_TO_PUBLISH - config.VARIATION_MSG_COUNT_TO_PUBLISH,
    config.MEAN_MSG_COUNT_TO_PUBLISH + config.VARIATION_MSG_COUNT_TO_PUBLISH)
