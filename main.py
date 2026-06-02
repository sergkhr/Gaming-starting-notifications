import argparse

from workers.core_worker import start_core_worker

from tests.test_runner import (
    run_all_tests,
    run_score_tests,
    run_action_tests,
    run_session_tests,
)


TEST_RUNNERS = {
    "0": run_all_tests,
    "1": run_score_tests,
    "2": run_action_tests,
    "3": run_session_tests,
}


TEST_NAMES = {
    "1": "Score tests",
    "2": "Action tests",
    "3": "Session tests",
}


def show_test_menu():

    print("\nAvailable test suites:\n")

    print("0 - Run all tests")

    for test_id, test_name in TEST_NAMES.items():
        print(f"{test_id} - {test_name}")

    print()

    selected = input("Select test suite: ").strip()

    return selected


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--test",
        nargs="?",
        const="-1",
        help="Run test suite"
    )

    args = parser.parse_args()

    #
    # Test mode
    #

    if args.test is not None:

        selected_test = args.test

        if selected_test == "-1":
            selected_test = show_test_menu()

        runner = TEST_RUNNERS.get(selected_test)

        if runner is None:

            print(
                f"Unknown test suite: {selected_test}"
            )

            return

        runner()

        return

    #
    # Normal mode
    #

    start_core_worker()


if __name__ == "__main__":
    main()