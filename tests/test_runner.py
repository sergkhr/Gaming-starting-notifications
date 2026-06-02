from tests.test_cases import (
    SCORE_TEST_CASES,
    ACTION_TEST_CASES,
    SESSION_TEST_CASES,
)

from logic.scorer import analyze_message
from logic.notifier_logic import determine_action
from logic.session_tracker import SessionTracker

from models.internal_message import InternalMessage

from datetime import datetime, timedelta


def run_score_tests():

    print("\n=== SCORE TESTS ===")

    for test_case in SCORE_TEST_CASES:

        result = analyze_message(
            test_case["text"]
        )

        print("\n" + "=" * 60)

        print(
            f"CASE: {test_case['name']}"
        )

        print(
            f"TEXT: {test_case['text']}"
        )

        print(
            f"SCORE: {result.score}"
        )

        print(
            f"REASONS: {result.reasons}"
        )

        print(
            f"GAMES: {result.matched_games}"
        )

        print(
            f"WORDS: {result.matched_words}"
        )


def run_action_tests():

    print("\n=== ACTION TESTS ===")

    for test_case in ACTION_TEST_CASES:

        action = determine_action(
            test_case["score"]
        )

        print("\n" + "=" * 60)

        print(
            f"CASE: {test_case['name']}"
        )

        print(
            f"SCORE: {test_case['score']}"
        )

        print(
            f"ACTION: {action}"
        )


def run_session_tests():

    print("\n=== SESSION TESTS ===")

    for test_case in SESSION_TEST_CASES:

        print("\n" + "=" * 60)
        print(f"CASE: {test_case['name']}")
        print()

        tracker = SessionTracker()

        base_time = datetime.now()

        last_session = None

        for index, raw_message in enumerate(test_case["messages"]):

            message = InternalMessage(
                source="test",
                message_id=f"{test_case['name']}_msg_{index + 1}",
                chat_id="test_chat",
                user_id=raw_message["user_id"],
                user_name=raw_message["user_name"],
                text=raw_message["text"],
                reply_to_message_id=raw_message.get("reply_to_message_id"),
                timestamp=base_time + timedelta(minutes=index),
            )

            result = analyze_message(message.text)

            session = tracker.process_message(
                message=message,
                result=result,
            )

            if session is not None:
                last_session = session

            print(f"MSG: {message.text}")
            print(f" -> score={result.score}")
            print(f" -> reasons={result.reasons}")
            print(f" -> games={result.matched_games}")

            if session is None:
                print(" -> session=None")
            else:
                print(f" -> session_id={session.session_id}")
                print(f" -> game={session.game}")
                print(f" -> session_score={session.total_score}")
                print(f" -> messages={len(session.messages)}")
                print(f" -> participants={session.participants}")
                print(f" -> declined={session.declined_users}")

            print()

        active_sessions = tracker.get_active_sessions()

        actual_sessions = len(active_sessions)

        if last_session is None and active_sessions:
            last_session = active_sessions[0]

        actual_messages = 0
        actual_participants = set()
        actual_declined_users = set()

        if last_session is not None:
            actual_messages = len(last_session.messages)
            actual_participants = last_session.participants
            actual_declined_users = last_session.declined_users

        expected_sessions = test_case["expected_sessions"]
        expected_messages = test_case["expected_messages"]
        expected_participants = test_case["expected_participants"]
        expected_declined_users = test_case["expected_declined_users"]

        checks = [
            (
                "sessions",
                actual_sessions,
                expected_sessions,
            ),
            (
                "messages",
                actual_messages,
                expected_messages,
            ),
            (
                "participants",
                actual_participants,
                expected_participants,
            ),
            (
                "declined_users",
                actual_declined_users,
                expected_declined_users,
            ),
        ]

        print("RESULT:")

        for check_name, actual_value, expected_value in checks:

            status = "PASS" if actual_value == expected_value else "FAIL"

            print(
                f" -> {check_name}: {status} "
                f"(actual={actual_value}, expected={expected_value})"
            )


def run_all_tests():

    run_score_tests()

    run_action_tests()

    run_session_tests()