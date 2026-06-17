from mobile_game_gift_center.events import RewardEvent, active_events


def test_event_verification_requires_https_source():
    event = RewardEvent("Example", "Launch Event", "https://example.com", "global", "2026-06-16")
    assert event.is_verifiable()


def test_active_events_excludes_expired_dates():
    events = [
        RewardEvent("A", "Active", "https://example.com", "global", "2026-06-16"),
        RewardEvent("B", "Expired", "https://example.com", "global", "2026-06-16", "2026-01-01"),
    ]
    assert [event.event for event in active_events(events)] == ["Active"]
