import pika

from config.settings import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_USER,
    RABBITMQ_PASSWORD,
)


class RabbitMQClient:

    def __init__(self):

        self.connection = None

        self.channel = None

    def connect(self):

        credentials = pika.PlainCredentials(
            RABBITMQ_USER,
            RABBITMQ_PASSWORD
        )

        parameters = pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT,
            credentials=credentials,
        )

        self.connection = pika.BlockingConnection(
            parameters
        )

        self.channel = self.connection.channel()

    def declare_queue(
        self,
        queue_name: str
    ):

        if self.channel is None:
            self.connect()

        self.channel.queue_declare(
            queue=queue_name,
            durable=True
        )

    def publish(
        self,
        queue_name: str,
        message: str
    ):

        if self.channel is None:
            self.connect()

        self.declare_queue(
            queue_name
        )

        self.channel.basic_publish(
            exchange="",
            routing_key=queue_name,
            body=message.encode("utf-8"),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )

    def consume(
        self,
        queue_name: str,
        callback
    ):

        if self.channel is None:
            self.connect()

        self.declare_queue(
            queue_name
        )

        def wrapped_callback(
            channel,
            method,
            properties,
            body
        ):

            message = body.decode("utf-8")

            try:
                callback(message)

                channel.basic_ack(
                    delivery_tag=method.delivery_tag
                )

            except Exception as error:

                print(
                    f"Error while processing message: {error}"
                )

                channel.basic_nack(
                    delivery_tag=method.delivery_tag,
                    requeue=False
                )

        self.channel.basic_qos(
            prefetch_count=1
        )

        self.channel.basic_consume(
            queue=queue_name,
            on_message_callback=wrapped_callback
        )

        print(
            f"Consuming queue: {queue_name}"
        )

        self.channel.start_consuming()

    def close(self):

        if self.connection is not None:
            self.connection.close()