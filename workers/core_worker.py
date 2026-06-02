from config.settings import (
    RABBITMQ_TELEGRAM_MESSAGES_QUEUE,
    RABBITMQ_DISCORD_NOTIFICATIONS_QUEUE,
)

from integrations.rabbitmq_client import RabbitMQClient

from logic.message_processor import MessageProcessor

from serializers.internal_message_serializer import (
    internal_message_from_json,
)

from serializers.notification_event_serializer import (
    notification_event_to_json,
)


class CoreWorker:

    def __init__(self):

        self.rabbitmq_client = RabbitMQClient()

        self.message_processor = MessageProcessor()

    def start(self):

        print("Core worker started")

        self.rabbitmq_client.consume(
            queue_name=RABBITMQ_TELEGRAM_MESSAGES_QUEUE,
            callback=self.process_raw_message,
        )

    def process_raw_message(
        self,
        raw_message: str
    ):

        print("Received message from RabbitMQ")

        internal_message = internal_message_from_json(
            raw_message
        )

        notification_event = (
            self.message_processor.process_message(
                internal_message
            )
        )

        if notification_event is None:

            print("No notification event created")

            return

        notification_json = notification_event_to_json(
            notification_event
        )

        self.rabbitmq_client.publish(
            queue_name=RABBITMQ_DISCORD_NOTIFICATIONS_QUEUE,
            message=notification_json,
        )

        print(
            "Notification event published to RabbitMQ"
        )


def start_core_worker():

    worker = CoreWorker()

    worker.start()