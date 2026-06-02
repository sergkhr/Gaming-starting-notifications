from telethon import TelegramClient

from config.settings import (
    TG_API_ID,
    TG_API_HASH,
    TG_SESSION_NAME,
)


def create_telegram_client() -> TelegramClient:

    if not TG_API_ID:
        raise ValueError(
            "TG_API_ID is not configured"
        )

    if not TG_API_HASH:
        raise ValueError(
            "TG_API_HASH is not configured"
        )

    return TelegramClient(
        TG_SESSION_NAME,
        TG_API_ID,
        TG_API_HASH,
    )