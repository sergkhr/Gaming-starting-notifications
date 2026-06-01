from models.score_result import ScoreResult

from config.rules import RULES

from logic.text_utils import (
    normalize_text,
    find_matches
)

from config.words import GAME_PATTERNS

from config.weights import GAME_DETECTED


def analyze_message(text: str) -> ScoreResult:

    normalized_text = normalize_text(text)

    result = ScoreResult()

    #
    # Games
    #

    for game_name, aliases in GAME_PATTERNS.items():

        found_aliases = find_matches(
            normalized_text,
            aliases
        )

        if found_aliases:

            result.score += GAME_DETECTED

            result.reasons.append("game_detected")

            result.matched_games.append(game_name)

            result.matched_words.extend(found_aliases)

    #
    # Rules
    #

    for rule in RULES:

        matched_patterns = find_matches(
            normalized_text,
            rule.patterns
        )

        if not matched_patterns:
            continue

        result.score += rule.score

        result.reasons.append(rule.name)

        result.matched_words.extend(matched_patterns)

    #
    # Cleanup duplicates
    #

    result.reasons = list(dict.fromkeys(result.reasons))

    result.matched_words = list(dict.fromkeys(result.matched_words))

    result.matched_games = list(dict.fromkeys(result.matched_games))

    return result