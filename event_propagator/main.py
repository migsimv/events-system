import logging
from .config import PropagatorConfig
from .event_loader import EventLoader
from .event_sender import EventSender
import time

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    config = PropagatorConfig.from_yaml("config/propagator_config.yaml")
    event_loader = EventLoader(config.events_file)
    events = event_loader.load_events()
    
    sender = EventSender(config.api_endpoint, events)

    logger.info(f"Starting event propagator with interval: {config.interval_seconds} seconds")
    while True:
        sender.send_random_event()
        time.sleep(config.interval_seconds)

if __name__ == "__main__":
    main()
