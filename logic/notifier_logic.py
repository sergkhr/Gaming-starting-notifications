from models.game_session import GameSession

from config.settings import (
    SESSION_NEW_NOTIFICATION_STEP,
    SESSION_MAX_SCORE,
)


def determine_action(session: GameSession) -> str:

    if session.total_score >= SESSION_MAX_SCORE:
        return "ignore"

    score_delta = (
        session.total_score
        - session.last_notification_sent_at_score
    )

    if score_delta >= SESSION_NEW_NOTIFICATION_STEP:
        return "notify"

    return "ignore"