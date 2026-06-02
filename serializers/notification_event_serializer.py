import json

from datetime import datetime

from models.notification_event import NotificationEvent


def notification_event_to_dict(
    event: NotificationEvent
) -> dict:
    """
    Convert NotificationEvent to dictionary for JSON serialization.
    """

    return {
        "session_id": event.session_id,

        "chat_id": event.chat_id,

        "game": event.game,

        "score": event.score,

        "participants_count": event.participants_count,

        "message_count": event.message_count,

        "last_activity": event.last_activity.isoformat(),

        "participants": event.participants,
    }


def notification_event_from_dict(
    data: dict
) -> NotificationEvent:
    """
    Convert dictionary to NotificationEvent.
    """

    last_activity = data["last_activity"]

    if isinstance(last_activity, str):
        last_activity = datetime.fromisoformat(last_activity)

    return NotificationEvent(
        session_id=str(data["session_id"]),

        chat_id=str(data["chat_id"]),

        game=str(data["game"]),

        score=int(data["score"]),

        participants_count=int(data["participants_count"]),

        message_count=int(data["message_count"]),

        last_activity=last_activity,

        participants=[
            str(participant)
            for participant in data.get("participants", [])
        ],
    )


def notification_event_to_json(
    event: NotificationEvent
) -> str:
    """
    Convert NotificationEvent to JSON string.
    """

    return json.dumps(
        notification_event_to_dict(event),
        ensure_ascii=False,
    )


def notification_event_from_json(
    raw_json: str
) -> NotificationEvent:
    """
    Convert JSON string to NotificationEvent.
    """

    data = json.loads(raw_json)

    return notification_event_from_dict(data)