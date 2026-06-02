from config.settings import (
    RABBITMQ_DISCORD_NOTIFICATIONS_QUEUE,
)

from integrations.discord_client import DiscordClient

from integrations.rabbitmq_client import RabbitMQClient

from serializers.notification_event_serializer import (
    notification_event_from_json,
)


def format_discord_message(event) -> str:
    """
    Convert NotificationEvent to Discord message text.
    """

    participants_text = "нет данных"

    if event.participants:
        participants_text = ", ".join(
            event.participants
        )

    return (
        f"🎮 Похоже, собираются играть\n\n"
        f"Игра: {event.game}\n"
        f"Score: {event.score}\n"
        f"Участников: {event.participants_count}\n"
        f"Сообщений в сессии: {event.message_count}\n"
        f"Участники: {participants_text}\n"
        f"Последняя активность: {event.last_activity.isoformat()}"
    )


class DiscordAdapter:

    def __init__(self):

        self.rabbitmq_client = RabbitMQClient()

        self.discord_client = DiscordClient()

    def start(self):

        print("Discord adapter started")

        self.rabbitmq_client.consume(
            queue_name=RABBITMQ_DISCORD_NOTIFICATIONS_QUEUE,
            callback=self.handle_notification,
        )

    def handle_notification(
        self,
        raw_message: str
    ):

        event = notification_event_from_json(
            raw_message
        )

        text = format_discord_message(
            event
        )

        self.discord_client.send_message(
            text
        )

        print("Notification sent to Discord")


def start_discord_adapter():

    adapter = DiscordAdapter()

    adapter.start()


if __name__ == "__main__":
    start_discord_adapter()