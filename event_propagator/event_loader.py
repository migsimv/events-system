import json
from typing import List, Dict, Any

class EventLoader:
    def __init__(self, events_file: str):
        self.events_file = events_file
        self.events: List[Dict[str, Any]] = []

    def load_events(self) -> List[Dict[str, Any]]:
        with open(self.events_file, 'r') as f:
            self.events = json.load(f)
        return self.events
