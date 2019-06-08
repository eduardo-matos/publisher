# Publisher

Publishes messages to specific queue on RabbitMQ

## Env variables

1. **`RABBITMQ_DESTINATION_QUEUE_NAME`**: RabbitMQ queue name which messages will be sent to.
1. `RABBITMQ_HOST` (default: `localhost`): RabbitMQ host.
1. `RABBITMQ_PORT` (default: `5672`): RabbitMQ port.
1. `RABBITMQ_USER` (default: `guest`): RabbitMQ username.
1. `RABBITMQ_PASS` (default: `guest`): RabbitMQ password.
1. `RABBITMQ_VHOST` (default: `/`): RabbitMQ host.
1. `APP_MIN_MSG_COUNT_TO_PUBLISH` (default: `0`): Minimum number of messages that will be sent to RabbitMQ.
1. `APP_MAX_MSG_COUNT_TO_PUBLISH` (default: `100`): Maximum number of messages that will be enqueued.

## Build

```sh
docker build . -t publisher
```

## Run

```sh
docker run \
 -e RABBITMQ_DESTINATION_QUEUE_NAME="spam" \
 -e RABBITMQ_HOST="localhost" \
 -e RABBITMQ_PORT="5672" \
 -e RABBITMQ_USER="guest" \
 -e RABBITMQ_PASS="guest" \
 -e RABBITMQ_VHOST="`/`):" \
 -e APP_MIN_MSG_COUNT_TO_PUBLISH="0" \
 -e APP_MAX_MSG_COUNT_TO_PUBLISH="100" \
 publisher
```

Make sure to use the `--net=host` option if RabbitMQ and MongoDB are running in the host network.
