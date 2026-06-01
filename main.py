import argparse

from tests.run_tests import run_tests


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--test",
        action="store_true",
        help="Run test cases"
    )

    args = parser.parse_args()

    if args.test:
        run_tests()
        return

    print("Notifier (nothing so far) started")


if __name__ == "__main__":
    main()