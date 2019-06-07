import os
import json
from datetime import datetime
import pika
from publisher.logger import logger 
from publisher.rabbitmq import send_to_queue
from publisher.random import sample_amount

msg_count_to_publish = sample_amount()
logger.info(f'Pulishing {msg_count_to_publish} messages')

for _ in range(msg_count_to_publish):
  send_to_queue({'started_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')})
