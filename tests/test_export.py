from mobile_game_gift_center.events import RewardEvent
from mobile_game_gift_center.export import export_events, load_events
import tempfile, os

def test_roundtrip():
    events = [RewardEvent("Game", "Event", "https://example.com", "global", "2026-06-16")]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        export_events(events, f.name)
        path = f.name
    loaded = load_events(path)
    os.unlink(path)
    assert loaded[0].game == "Game"
