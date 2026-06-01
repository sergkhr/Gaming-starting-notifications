import re


def normalize_text(text: str) -> str:
    """
    Normalize message text for further analysis.

    Steps:
    1. Lowercase.
    2. Remove line breaks.
    3. Remove duplicated spaces.
    4. Remove punctuation.
    5. Trim spaces.
    """

    if not text:
        return ""

    text = text.lower()

    text = text.replace("\n", " ")
    text = text.replace("\r", " ")

    text = re.sub(r"[^\w\s]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def contains_any(text: str, patterns: list[str]) -> bool:
    """
    Check if text contains any pattern.
    """

    for pattern in patterns:
        if pattern in text:
            return True

    return False


def count_matches(text: str, patterns: list[str]) -> int:
    """
    Count matched patterns.
    """

    count = 0

    for pattern in patterns:
        if pattern in text:
            count += 1

    return count