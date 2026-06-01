from dataclasses import dataclass


@dataclass
class Rule:
    name: str
    score: int
    patterns: list[str]