import time

import pika

from pika.exceptions import (
    AMQPConnectionError,
    ChannelClosedByBroker,
    ConnectionClosed,
    StreamLostError,
)

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

        self.close()

        credentials = pika.PlainCredentials(
            RABBITMQ_USER,
            RABBITMQ_PASSWORD
        )

        parameters = pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT,
            credentials=credentials,
            heartbeat=30,
            blocked_connection_timeout=30,
        )

        self.connection = pika.BlockingConnection(
            parameters
        )

        self.channel = self.connection.channel()

    def ensure_connection(self):

        if self.connection is None or self.connection.is_closed:
            self.connect()
            return

        if self.channel is None or self.channel.is_closed:
            self.channel = self.connection.channel()

    def declare_queue(
        self,
        queue_name: str
    ):

        self.ensure_connection()

        self.channel.queue_declare(
            queue=queue_name,
            durable=True
        )

    def publish(
        self,
        queue_name: str,
        message: str
    ):

        try:

            self._publish_once(
                queue_name=queue_name,
                message=message,
            )

        except (
            AMQPConnectionError,
            ConnectionClosed,
            StreamLostError,
            ChannelClosedByBroker,
            ConnectionResetError,
        ):

            print(
                "RabbitMQ connection lost while publishing. Reconnecting..."
            )

            self.connect()

            self._publish_once(
                queue_name=queue_name,
                message=message,
            )

    def _publish_once(
        self,
        queue_name: str,
        message: str
    ):

        self.ensure_connection()

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

        self.ensure_connection()

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

        while True:

            try:

                self.channel.start_consuming()

            except (
                AMQPConnectionError,
                ConnectionClosed,
                StreamLostError,
                ConnectionResetError,
            ) as error:

                print(
                    f"RabbitMQ consuming connection lost: {error}"
                )

                print(
                    "Reconnecting to RabbitMQ..."
                )

                time.sleep(5)

                self.connect()

                self.declare_queue(
                    queue_name
                )

                self.channel.basic_qos(
                    prefetch_count=1
                )

                self.channel.basic_consume(
                    queue=queue_name,
                    on_message_callback=wrapped_callback
                )

    def close(self):

        try:

            if self.connection is not None and self.connection.is_open:
                self.connection.close()

        except Exception:
            pass

        self.connection = None

        self.channel = None