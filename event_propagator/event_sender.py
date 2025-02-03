import random
import requests
from typing import List, Dict, Any
import time
import logging

class EventSender:
    def __init__(self, api_endpoint: str, events: List[Dict[str, Any]]):
        self.api_endpoint = api_endpoint
        self.events = events
        self.logger = logging.getLogger(__name__)

    def send_random_event(self) -> None:
        event = random.choice(self.events)
        try:
            response = requests.post(self.api_endpoint, json=event)
            response.raise_for_status()
            self.logger.info(f"Sent event: {event}")
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to send event: {event}, error: {e}")
