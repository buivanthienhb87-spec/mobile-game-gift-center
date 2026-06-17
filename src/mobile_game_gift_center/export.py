from __future__ import annotations
import json
from pathlib import Path
from .events import RewardEvent

def export_events(events: list[RewardEvent], output_path: str) -> None:
    data = [{"game": e.game, "event": e.event, "source_url": e.source_url, "region": e.region, "reviewed_at": e.reviewed_at, "expires_at": e.expires_at} for e in events]
    Path(output_path).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

def load_events(path: str) -> list[RewardEvent]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return [RewardEvent(**item) for item in data]
