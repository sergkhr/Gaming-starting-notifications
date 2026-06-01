from dataclasses import dataclass


@dataclass
class NotificationRule:

    name: str

    action: str

    min_score: int