from dataclasses import dataclass, field

from datetime import datetime

from models.internal_message import InternalMessage


@dataclass
class GameSession:

    session_id: str

    chat_id: str

    game: str

    created_at: datetime

    last_activity: datetime

    creator_user_id: str

    creator_user_name: str

    messages: list[InternalMessage] = field(default_factory=list)

    participants: set[str] = field(default_factory=set)

    declined_users: set[str] = field(default_factory=set)

    total_score: int = 0

    last_notification_sent_at_score: int = 0