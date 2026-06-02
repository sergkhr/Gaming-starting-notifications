import json

from datetime import datetime

from models.internal_message import InternalMessage


def internal_message_to_dict(
    message: InternalMessage
) -> dict:
    """
    Convert InternalMessage to dictionary for JSON serialization.
    """

    return {
        "source": message.source,

        "message_id": message.message_id,

        "chat_id": message.chat_id,

        "user_id": message.user_id,

        "user_name": message.user_name,

        "text": message.text,

        "reply_to_message_id": message.reply_to_message_id,

        "timestamp": message.timestamp.isoformat(),
    }


def internal_message_from_dict(
    data: dict
) -> InternalMessage:
    """
    Convert dictionary to InternalMessage.
    """

    timestamp = data["timestamp"]

    if isinstance(timestamp, str):
        timestamp = datetime.fromisoformat(timestamp)

    return InternalMessage(
        source=str(data["source"]),

        message_id=str(data["message_id"]),

        chat_id=str(data["chat_id"]),

        user_id=str(data["user_id"]),

        user_name=str(data["user_name"]),

        text=str(data["text"]),

        reply_to_message_id=(
            str(data["reply_to_message_id"])
            if data.get("reply_to_message_id") is not None
            else None
        ),

        timestamp=timestamp,
    )


def internal_message_to_json(
    message: InternalMessage
) -> str:
    """
    Convert InternalMessage to JSON string.
    """

    return json.dumps(
        internal_message_to_dict(message),
        ensure_ascii=False,
    )


def internal_message_from_json(
    raw_json: str
) -> InternalMessage:
    """
    Convert JSON string to InternalMessage.
    """

    data = json.loads(raw_json)

    return internal_message_from_dict(data)