import requests

from config.settings import DISCORD_WEBHOOK_URL


class DiscordClient:

    def __init__(self):

        if not DISCORD_WEBHOOK_URL:
            raise ValueError(
                "DISCORD_WEBHOOK_URL is not configured"
            )

        self.webhook_url = DISCORD_WEBHOOK_URL

    def send_message(
        self,
        text: str
    ):

        response = requests.post(
            self.webhook_url,
            json={
                "content": text
            },
            timeout=10,
        )

        response.raise_for_status()