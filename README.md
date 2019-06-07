# Publisher

Publishes messages to specific queue on RabbitMQ

## Env variables

1. `RABBITMQ_DESTINATION_QUEUE_NAME`: RabbitMQ queue name which messages will be sent to.
1. `RABBITMQ_HOST` (default: `localhost`): RabbitMQ host.
1. `RABBITMQ_PORT` (default: `5672`): RabbitMQ port.
1. `RABBITMQ_USER` (default: `guest`): RabbitMQ username.
1. `RABBITMQ_PASS` (default: `guest`): RabbitMQ password.
1. `RABBITMQ_VHOST` (default: `/`): RabbitMQ host.
1. `APP_MEAN_MSG_COUNT_TO_PUBLISH` (default: `100`): Average number of messages that will be sent to RabbitMQ.
1. `APP_VARIATION_MSG_COUNT_TO_PUBLISH` (default: `5`): Maximum value which `APP_MEAN_MSG_COUNT_TO_PUBLISH` will vary.
