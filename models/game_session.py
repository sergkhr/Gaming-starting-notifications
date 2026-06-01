from dataclasses import dataclass, field

from datetime import datetime


@dataclass
class GameSession:

    game: str

    created_at: datetime

    last_activity: datetime

    messages: list[str] = field(default_factory=list)

    participants: set[str] = field(default_factory=set)

    total_score: int = 0