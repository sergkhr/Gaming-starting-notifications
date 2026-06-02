from datetime import datetime

from telethon import events

from config.settings import (
    RABBITMQ_TELEGRAM_MESSAGES_QUEUE,
    TG_TARGET_CHAT_ID,
)

from integrations.rabbitmq_client import RabbitMQClient

from integrations.telegram_client import create_telegram_client

from models.internal_message import InternalMessage

from serializers.internal_message_serializer import (
    internal_message_to_json,
)


def telegram_event_to_internal_message(
    event
) -> InternalMessage:

    message = event.message

    sender = message.sender

    user_id = ""

    user_name = "unknown"

    if sender is not None:

        user_id = str(
            getattr(
                sender,
                "id",
                ""
            )
        )

        first_name = getattr(
            sender,
            "first_name",
            ""
        ) or ""

        last_name = getattr(
            sender,
            "last_name",
            ""
        ) or ""

        username = getattr(
            sender,
            "username",
            ""
        ) or ""

        full_name = (
            f"{first_name} {last_name}"
        ).strip()

        user_name = (
            full_name
            or username
            or user_id
            or "unknown"
        )

    reply_to_message_id = None

    if message.reply_to_msg_id is not None:
        reply_to_message_id = str(
            message.reply_to_msg_id
        )

    text = message.message or ""

    return InternalMessage(
        source="telegram",

        message_id=str(message.id),

        chat_id=str(event.chat_id),

        user_id=user_id,

        user_name=user_name,

        text=text,

        reply_to_message_id=reply_to_message_id,

        timestamp=message.date or datetime.now(),
    )


class TelegramAdapter:

    def __init__(self):

        self.telegram_client = create_telegram_client()

        self.rabbitmq_client = RabbitMQClient()

    async def start(self):

        print("Telegram adapter started")

        @self.telegram_client.on(
            events.NewMessage()
        )
        async def handler(event):

            if TG_TARGET_CHAT_ID:

                if str(event.chat_id) != str(TG_TARGET_CHAT_ID):
                    return

            internal_message = (
                telegram_event_to_internal_message(
                    event
                )
            )

            message_json = internal_message_to_json(
                internal_message
            )

            try:

                self.rabbitmq_client.publish(
                    queue_name=RABBITMQ_TELEGRAM_MESSAGES_QUEUE,
                    message=message_json,
                )

                print(
                    f"Telegram message published: {internal_message.text}"
                )

            except Exception as error:

                print(
                    f"Failed to publish Telegram message to RabbitMQ: {error}"
                )

        await self.telegram_client.start()

        await self.telegram_client.run_until_disconnected()


def start_telegram_adapter():

    adapter = TelegramAdapter()

    with adapter.telegram_client:

        adapter.telegram_client.loop.run_until_complete(
            adapter.start()
        )


if __name__ == "__main__":
    start_telegram_adapter()