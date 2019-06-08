import os
import json
from datetime import datetime
from random import randint
import pika
from publisher import config
from publisher.logger import logger 
from publisher.rabbitmq import send_to_queue

msg_count_to_publish = randint(config.MIN_MSG_COUNT_TO_PUBLISH, config.MAX_MSG_COUNT_TO_PUBLISH)
logger.info(f'Pulishing {msg_count_to_publish} messages')

for _ in range(msg_count_to_publish):
  send_to_queue({'started_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')})
