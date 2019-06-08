import os

HOST = os.environ.get('RABBITMQ_HOST', 'localhost')
PORT = os.environ.get('RABBITMQ_PORT', '5672')
USER = os.environ.get('RABBITMQ_USER', 'guest')
PASS = os.environ.get('RABBITMQ_PASS', 'guest')
VHOST = os.environ.get('RABBITMQ_VHOST', '/')

MIN_MSG_COUNT_TO_PUBLISH = int(os.environ.get('APP_MIN_MSG_COUNT_TO_PUBLISH', 0))
MAX_MSG_COUNT_TO_PUBLISH = int(os.environ.get('APP_MAX_MSG_COUNT_TO_PUBLISH', 100))

DESTINATION_QUEUE_NAME = os.environ['RABBITMQ_DESTINATION_QUEUE_NAME']