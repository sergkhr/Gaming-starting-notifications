from dataclasses import dataclass
from datetime import datetime

@dataclass
class InternalMessage:
    source: str

    message_id: str

    chat_id: str

    user_id: str
    user_name: str

    text: str

    reply_to_message_id: str | None

    timestamp: datetime