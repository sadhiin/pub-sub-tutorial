# trading_system/src/utils/serializers.py
# (Optional)  Example of a custom serializer.  The code in market_data_producer.py
# and trading_consumer.py uses json, which is sufficient for this example,
# but this shows how you might create a more specialized one if needed.
import json
from datetime import datetime
from dataclasses import asdict
from src.core.event_model import MarketEvent
from typing import Any, Dict

def market_event_serializer(event: MarketEvent) -> bytes:
    """
    Serializes a MarketEvent object into a JSON string encoded as bytes.

    Args:
        event: The MarketEvent to serialize.

    Returns:
        bytes: The serialized event.
    """
    #  Use the to_dict method of the MarketEvent for consistency
    event_dict = event.to_dict()
    return json.dumps(event_dict).encode('utf-8')

def market_event_deserializer(data: bytes) -> MarketEvent:
    """
    Deserializes a bytes object into a MarketEvent object.

    Args:
        data: The bytes to deserialize.

    Returns:
        MarketEvent: The deserialized event.
    """
    #  Use the from_dict method of MarketEvent for consistency and correctness
    event_dict = json.loads(data.decode('utf-8'))
    return MarketEvent.from_dict(event_dict)

if __name__ == '__main__':
    # Example usage:
    sample_event = MarketEvent(symbol="TEST", price=123.45, volume=100, timestamp=datetime.now())
    serialized_event = market_event_serializer(sample_event)
    print(f"Serialized: {serialized_event}")
    deserialized_event = market_event_deserializer(serialized_event)
    print(f"Deserialized: {deserialized_event}")
    assert sample_event == deserialized_event