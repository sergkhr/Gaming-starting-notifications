from datetime import datetime

from config.settings import RABBITMQ_TELEGRAM_MESSAGES_QUEUE

from integrations.rabbitmq_client import RabbitMQClient

from models.internal_message import InternalMessage

from serializers.internal_message_serializer import (
    internal_message_to_json,
)


def main():

    message = InternalMessage(
        source="manual_test",

        message_id="test-message-1",

        chat_id="test-chat",

        user_id="test-user-1",

        user_name="Test User",

        text="го дота",

        reply_to_message_id=None,

        timestamp=datetime.now(),
    )

    message_json = internal_message_to_json(
        message
    )

    rabbitmq_client = RabbitMQClient()

    rabbitmq_client.publish(
        queue_name=RABBITMQ_TELEGRAM_MESSAGES_QUEUE,
        message=message_json,
    )

    rabbitmq_client.close()

    print("Test message published")


if __name__ == "__main__":
    main()