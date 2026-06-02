IMMEDIATE_NOTIFICATION_SCORE = 10 #that's basically just notify score sry for confusion

WATCH_SESSION_SCORE = 5

SESSION_TIMEOUT_MINUTES = 30

SESSION_NEW_NOTIFICATION_STEP = 10

SESSION_MAX_SCORE = 50


import os

RABBITMQ_HOST = "rabbitmq"
RABBITMQ_PORT = 5672

RABBITMQ_USER = os.getenv(
    "RABBITMQ_DEFAULT_USER",
    "admin"
)

RABBITMQ_PASSWORD = os.getenv(
    "RABBITMQ_DEFAULT_PASS",
    "admin"
)

RABBITMQ_TELEGRAM_MESSAGES_QUEUE = "telegram.messages"
RABBITMQ_DISCORD_NOTIFICATIONS_QUEUE = "discord.notifications"


DISCORD_WEBHOOK_URL = os.getenv(
    "DISCORD_WEBHOOK_URL",
    ""
)


TG_API_ID = int(
    os.getenv(
        "TG_API_ID",
        "0"
    )
)

TG_API_HASH = os.getenv(
    "TG_API_HASH",
    ""
)

TG_SESSION_NAME = os.getenv(
    "TG_SESSION_NAME",
    "telegram_session"
)

TG_TARGET_CHAT_ID = os.getenv(
    "TG_TARGET_CHAT_ID",
    ""
)