from datetime import datetime
from datetime import timedelta

from models.game_session import GameSession
from models.score_result import ScoreResult

from config.settings import SESSION_TIMEOUT_MINUTES


class SessionTracker:

    def __init__(self):

        self.sessions: list[GameSession] = []

    def cleanup_expired_sessions(self):

        now = datetime.now()

        self.sessions = [
            session

            for session in self.sessions

            if now - session.last_activity < timedelta(minutes=SESSION_TIMEOUT_MINUTES)
        ]

    def find_session(
        self,
        game: str
    ) -> GameSession | None:

        self.cleanup_expired_sessions()

        for session in self.sessions:

            if session.game == game:
                return session

        return None

    def process_message(
        self,
        text: str,
        result: ScoreResult
    ) -> GameSession | None:

        self.cleanup_expired_sessions()

        #
        # Message does not contain a game
        #

        if not result.matched_games:
            return None

        game = result.matched_games[0]

        session = self.find_session(game)

        now = datetime.now()

        #
        # Create session
        #

        if session is None:

            session = GameSession(
                game=game,
                created_at=now,
                last_activity=now,
            )

            self.sessions.append(session)

        #
        # Update session
        #

        session.last_activity = now

        session.messages.append(text)

        session.total_score += result.score

        return session

    def get_active_sessions(self) -> list[GameSession]:

        self.cleanup_expired_sessions()

        return self.sessions