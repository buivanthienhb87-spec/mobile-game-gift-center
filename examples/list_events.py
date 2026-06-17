import json
from pathlib import Path

for event in json.loads(Path('data/events.json').read_text(encoding='utf-8')):
    print(f"{event['game']}: {event['event']} [{event['region']}]")
