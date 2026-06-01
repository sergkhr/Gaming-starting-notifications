from tests.test_cases import TEST_CASES

from logic.scorer import analyze_message


def run_tests():

    print("Running tests...")

    for test_case in TEST_CASES:

        result = analyze_message(test_case["text"])

        print()
        print("=" * 60)

        print(f"CASE: {test_case['name']}")
        print(f"TEXT: {test_case['text']}")

        print()

        print(f"SCORE: {result.score}")

        print(f"REASONS: {result.reasons}")

        print(f"MATCHED GAMES: {result.matched_games}")

        print(f"MATCHED WORDS: {result.matched_words}")

    print()
    print("=" * 60)
    print("Finished")