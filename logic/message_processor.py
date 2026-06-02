from models.internal_message import InternalMessage

from models.notification_event import NotificationEvent

from logic.scorer import analyze_message

from logic.session_tracker import SessionTracker

from logic.notifier_logic import determine_action

from logic.notification_builder import (
    build_notification_event
)


class MessageProcessor:

    def __init__(self):

        self.session_tracker = SessionTracker()

    def process_message(
        self,
        message: InternalMessage
    ) -> NotificationEvent | None:

        #
        # Analyze message
        #

        score_result = analyze_message(
            message.text
        )

        #
        # Update session
        #

        session = self.session_tracker.process_message(
            message,
            score_result
        )

        if session is None:
            return None

        #
        # Determine action
        #

        action = determine_action(
            session
        )

        if action != "notify":
            return None

        #
        # Build notification
        #

        notification_event = (
            build_notification_event(
                session
            )
        )

        return notification_event