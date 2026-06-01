from __future__ import annotations

from datetime import datetime, timedelta
from uuid import uuid4

from config.settings import (
    SESSION_TIMEOUT_MINUTES,
    SESSION_MAX_SCORE,
)

from models.game_session import GameSession
from models.internal_message import InternalMessage
from models.score_result import ScoreResult


class SessionTracker:
    def __init__(self) -> None:
        self.sessions: list[GameSession] = []

    def process_message(
        self,
        message: InternalMessage,
        result: ScoreResult,
    ) -> GameSession | None:
        now = message.timestamp

        self.cleanup_expired_sessions(now)

        session = self.find_session_by_reply(message)

        if session is None:
            session = self.find_session_by_game(message, result)

        if session is None:
            session = self.find_recent_session(message, result)

        if session is None:
            matched_games = result.matched_games

            if not matched_games:
                return None

            session = self.create_session(
                message=message,
                game=matched_games[0],
            )

        self.update_session(
            session=session,
            message=message,
            result=result,
        )

        return session

    def create_session(
        self,
        message: InternalMessage,
        game: str,
    ) -> GameSession:
        session = GameSession(
            session_id=str(uuid4()),
            chat_id=message.chat_id,
            game=game,
            created_at=message.timestamp,
            last_activity=message.timestamp,
            creator_user_id=message.user_id,
            creator_user_name=message.user_name,
        )

        self.sessions.append(session)

        return session

    def find_session_by_reply(
        self,
        message: InternalMessage,
    ) -> GameSession | None:
        if message.reply_to_message_id is None:
            return None

        for session in self.sessions:
            if session.chat_id != message.chat_id:
                continue

            for session_message in session.messages:
                if session_message.message_id == message.reply_to_message_id:
                    return session

        return None

    def find_session_by_game(
        self,
        message: InternalMessage,
        result: ScoreResult,
    ) -> GameSession | None:
        matched_games = result.matched_games

        if not matched_games:
            return None

        for session in self.sessions:
            if session.chat_id != message.chat_id:
                continue

            if session.game in matched_games:
                return session

        return None

    def find_recent_session(
        self,
        message: InternalMessage,
        result: ScoreResult,
    ) -> GameSession | None:
        reasons = result.reasons

        if not self._has_context_reaction(reasons):
            return None

        candidates: list[GameSession] = []

        for session in self.sessions:
            if session.chat_id != message.chat_id:
                continue

            candidates.append(session)

        if not candidates:
            return None

        return max(
            candidates,
            key=lambda session: session.last_activity,
        )

    def update_session(
        self,
        session: GameSession,
        message: InternalMessage,
        result: ScoreResult,
    ) -> None:
        if not self._session_contains_message(session, message.message_id):
            session.messages.append(message)

        session.last_activity = message.timestamp

        score = result.score
        session.total_score = min(
            SESSION_MAX_SCORE,
            session.total_score + score,
        )

        self.update_participants(
            session=session,
            message=message,
            result=result,
        )

    def update_participants(
        self,
        session: GameSession,
        message: InternalMessage,
        result: ScoreResult,
    ) -> None:
        reasons = result.reasons

        if "positive_response" in reasons:
            session.participants.add(message.user_id)
            session.declined_users.discard(message.user_id)

        if "negative_response" in reasons:
            session.declined_users.add(message.user_id)
            session.participants.discard(message.user_id)

    def cleanup_expired_sessions(
        self,
        now: datetime | None = None,
    ) -> None:
        if now is None:
            now = datetime.now()

        self.sessions = [
            session
            for session in self.sessions
            if now - session.last_activity < timedelta(
                minutes=SESSION_TIMEOUT_MINUTES,
            )
        ]

    def get_active_sessions(self) -> list[GameSession]:
        self.cleanup_expired_sessions()
        return self.sessions

    def _has_context_reaction(
        self,
        reasons: list[str],
    ) -> bool:
        context_reasons = {
            "positive_response",
            "soon_response",
            "negative_response",
        }

        return any(
            reason in context_reasons
            for reason in reasons
        )

    def _session_contains_message(
        self,
        session: GameSession,
        message_id: str,
    ) -> bool:
        return any(
            message.message_id == message_id
            for message in session.messages
        )