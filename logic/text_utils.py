import re


def normalize_text(text: str) -> str:
    """
    Normalize message text for further analysis.
    """

    if not text:
        return ""

    text = text.lower()

    text = text.replace("\n", " ")
    text = text.replace("\r", " ")

    text = re.sub(r"[^\w\s]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def find_matches(
    text: str,
    patterns: list[str]
) -> list[str]:
    """
    Find patterns as separate words or phrases.
    Prevent matching inside other words.
    """

    matches = []

    for pattern in patterns:

        escaped_pattern = re.escape(pattern)

        regex = rf"\b{escaped_pattern}\b"

        if re.search(regex, text):
            matches.append(pattern)

    return matches