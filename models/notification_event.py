from dataclasses import dataclass

from datetime import datetime


@dataclass
class NotificationEvent:

    session_id: str

    chat_id: str

    game: str

    score: int

    participants_count: int

    message_count: int

    last_activity: datetime

    participants: list[str]