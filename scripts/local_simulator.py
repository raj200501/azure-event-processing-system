#!/usr/bin/env python3
"""Local simulator for the Azure event processing pipeline.

This intentionally mirrors the README architecture (ingestion -> processing -> results)
without requiring Azure resources. It's used by scripts/run_local.sh and smoke tests.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Iterable, List


@dataclass
class Event:
    event_id: str
    payload: str
    created_at: str


@dataclass
class ProcessedEvent:
    event_id: str
    payload: str
    processed_at: str
    prediction: float


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def ingest_events(base_payload: str, count: int) -> List[Event]:
    events: List[Event] = []
    for index in range(count):
        event_id = f"evt-{index + 1}"
        payload = f"{base_payload}-{index + 1}"
        events.append(Event(event_id=event_id, payload=payload, created_at=utc_now_iso()))
    return events


def run_prediction(payload: str) -> float:
    """Deterministic pseudo-prediction for demo purposes."""
    seed = sum(ord(ch) for ch in payload)
    return round((seed % 100) / 100.0, 2)


def process_events(events: Iterable[Event]) -> List[ProcessedEvent]:
    processed: List[ProcessedEvent] = []
    for event in events:
        prediction = run_prediction(event.payload)
        processed.append(
            ProcessedEvent(
                event_id=event.event_id,
                payload=f"{event.payload}-processed",
                processed_at=utc_now_iso(),
                prediction=prediction,
            )
        )
    return processed


def emit_results(processed_events: Iterable[ProcessedEvent]) -> None:
    for event in processed_events:
        print(
            json.dumps(
                {
                    "event_id": event.event_id,
                    "payload": event.payload,
                    "processed_at": event.processed_at,
                    "prediction": event.prediction,
                }
            )
        )


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Local event processing simulator")
    parser.add_argument("--count", type=int, default=3, help="Number of events to simulate")
    parser.add_argument(
        "--payload",
        default=os.environ.get("EVENT_PAYLOAD", "sample-event"),
        help="Base payload for the events",
    )
    return parser.parse_args(argv)


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    print("Starting local event processing simulator")
    events = ingest_events(args.payload, args.count)
    print(f"Ingested {len(events)} events")
    processed = process_events(events)
    print(f"Processed {len(processed)} events")
    emit_results(processed)
    print("Pipeline complete")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
