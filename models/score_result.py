from dataclasses import dataclass, field


@dataclass
class ScoreResult:

    score: int = 0

    reasons: list[str] = field(default_factory=list)

    matched_words: list[str] = field(default_factory=list)

    matched_games: list[str] = field(default_factory=list)