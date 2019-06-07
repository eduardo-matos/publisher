import json
import pika
from publisher import config

connection = pika.BlockingConnection(pika.ConnectionParameters(
  host=config.HOST,
  port=config.PORT,
  virtual_host=config.VHOST,
  credentials=pika.PlainCredentials(config.USER, config.PASS)
))

channel = connection.channel()
channel.queue_declare(queue=config.DESTINATION_QUEUE_NAME, durable=True)

def send_to_queue(msg, queue=config.DESTINATION_QUEUE_NAME):
  channel.basic_publish(exchange='', routing_key=config.DESTINATION_QUEUE_NAME, body=json.dumps(msg))
