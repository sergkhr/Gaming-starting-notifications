from models.notification_rule import NotificationRule

from config.settings import (
    IMMEDIATE_NOTIFICATION_SCORE,
    WATCH_SESSION_SCORE
)

NOTIFICATION_RULES = [

    NotificationRule(
        name="notify",
        action="notify",
        min_score=IMMEDIATE_NOTIFICATION_SCORE
    ),

    NotificationRule(
        name="watch",
        action="watch",
        min_score=WATCH_SESSION_SCORE
    )
]