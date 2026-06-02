from models.game_session import GameSession

from models.notification_event import NotificationEvent


def build_notification_event(
    session: GameSession
) -> NotificationEvent:

    return NotificationEvent(

        session_id=session.session_id,

        chat_id=session.chat_id,

        game=session.game,

        score=session.total_score,

        participants_count=len(
            session.participants
        ),

        message_count=len(
            session.messages
        ),

        last_activity=session.last_activity,

        participants=list(
            session.participants
        ),
    )