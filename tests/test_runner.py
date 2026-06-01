from tests.test_cases import (
    SCORE_TEST_CASES,
    ACTION_TEST_CASES,
    SESSION_TEST_CASES,
)

from logic.scorer import analyze_message

from logic.notifier_logic import determine_action


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

        print(
            f"CASE: {test_case['name']}"
        )

        print()

        for message in test_case["messages"]:

            print(
                f"not implemented test MSG: {message}"
            )

            result = analyze_message(
                message
            )

            action = determine_action(
                result.score
            )

            print(
                f" -> score={result.score}"
            )

            print(
                f" -> action={action}"
            )


def run_all_tests():

    run_score_tests()

    run_action_tests()

    run_session_tests()