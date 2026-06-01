from models.rule import Rule

from config.words import (
    STRONG_INVITE_PATTERNS,
    MEDIUM_INTENT_PATTERNS,
    VIBE_PATTERNS,
    POSITIVE_RESPONSE_PATTERNS,
    SOON_RESPONSE_PATTERNS,
    NEGATIVE_RESPONSE_PATTERNS,
    URGENCY_PATTERNS,
    VOICE_AND_DISCORD_PATTERNS,
    WEAK_NEGATIVE_CONTEXT_PATTERNS,
)

from config.weights import (
    STRONG_INVITE,
    MEDIUM_INTENT,
    VIBE_MARKER,
    POSITIVE_RESPONSE,
    SOON_RESPONSE,
    NEGATIVE_RESPONSE,
    URGENCY,
    VOICE_OR_DISCORD,
    WEAK_NEGATIVE_CONTEXT,
)


RULES = [

    Rule(
        name="strong_invite",
        score=STRONG_INVITE,
        patterns=STRONG_INVITE_PATTERNS,
    ),

    Rule(
        name="medium_intent",
        score=MEDIUM_INTENT,
        patterns=MEDIUM_INTENT_PATTERNS,
    ),

    Rule(
        name="vibe_marker",
        score=VIBE_MARKER,
        patterns=VIBE_PATTERNS,
    ),

    Rule(
        name="positive_response",
        score=POSITIVE_RESPONSE,
        patterns=POSITIVE_RESPONSE_PATTERNS,
    ),

    Rule(
        name="soon_response",
        score=SOON_RESPONSE,
        patterns=SOON_RESPONSE_PATTERNS,
    ),

    Rule(
        name="negative_response",
        score=NEGATIVE_RESPONSE,
        patterns=NEGATIVE_RESPONSE_PATTERNS,
    ),

    Rule(
        name="urgency",
        score=URGENCY,
        patterns=URGENCY_PATTERNS,
    ),

    Rule(
        name="voice_or_discord",
        score=VOICE_OR_DISCORD,
        patterns=VOICE_AND_DISCORD_PATTERNS,
    ),

    Rule(
        name="weak_negative_context",
        score=WEAK_NEGATIVE_CONTEXT,
        patterns=WEAK_NEGATIVE_CONTEXT_PATTERNS,
    ),
]