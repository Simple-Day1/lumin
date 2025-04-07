from dataclasses import dataclass


@dataclass(frozen=True)
class Reaction:
    reaction: str
