from dataclasses import dataclass


@dataclass(frozen=True)
class Phone:
    phone: str


@dataclass(frozen=True)
class Date:
    date: str
