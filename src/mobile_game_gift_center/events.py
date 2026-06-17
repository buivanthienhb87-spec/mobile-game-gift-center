from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class RewardEvent:
    game: str
    event: str
    source_url: str
    region: str
    reviewed_at: str
    expires_at: str | None = None

    def is_verifiable(self) -> bool:
        return self.source_url.startswith("https://") and bool(self.reviewed_at)


def active_events(events: list[RewardEvent]) -> list[RewardEvent]:
    return [event for event in events if event.expires_at is None]
