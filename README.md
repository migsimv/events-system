# Event System Documentation

## Overview

This project consists of two Python services that communicate with each other: an Event Propagator that periodically sends predefined event payloads and an Event Consumer that receives and stores these events.

# Services

1. Event Propagator
    
    The Event Propagator periodically sends predefined JSON objects to a configured HTTP API endpoint:
    
        Sends events at a configurable interval (in seconds).
        
        The API endpoint is configurable.
        
        Reads predefined JSON events from a file.
        
        The location of the JSON file is configurable.
        
        Selects a random event from the list for each transmission.

    Configuration:
    
        Configuration is stored in config/propagator_config.yaml:
    
            interval_seconds: 5
            api_endpoint: "http://localhost:8000/event"
            events_file: "events/events.json"
    
        Running the Service:
        
            poetry install  # Install dependencies
            poetry run python -m event_propagator.main  

2. Event Consumer
    
    The Event Consumer provides an HTTP API that accepts incoming JSON event payloads and persists them to a database:
    
        Exposes an HTTP API on a configurable port.
        
        Stores received events in a database (SQLite by default).
        
        Accepts only valid JSON payloads with event_type and event_payload as strings.
    
    Configuration:
    
        Configuration is stored in config/consumer_config.yaml:
        
        port: 8000
        database_url: "sqlite:///events.db"
    
    Running the Service:
    
        poetry install 
        poetry run python -m event_consumer.main 

# Dependencies Management

This project uses Poetry for dependency management. Install dependencies with:

    poetry install
    
    Running the Services
    
    Start the Event Consumer:
    
    poetry run python -m event_consumer.main
    
    Start the Event Propagator:
    
    poetry run python -m event_propagator.main
    
    API Reference
    
    Event Consumer API
    
    Endpoint: POST /event

    Payload:
    
    {
      "event_type": "string",
      "event_payload": "string"
    }
    
    Response:
    
    { "status": "success" }
    
