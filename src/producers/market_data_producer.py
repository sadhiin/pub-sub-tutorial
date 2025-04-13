# trading_system/src/producers/market_data_producer.py
# Simulates market data and sends it to Kafka
import random
from datetime import datetime
from time import sleep
from typing import List, Generator

from kafka import KafkaProducer
from src.core.event_model import MarketEvent
from src.config.settings import KAFKA_BROKERS, MARKET_EVENTS_TOPIC
import json

def market_data_generator(symbols: List[str], num_events: int) -> Generator[MarketEvent, None, None]:
    """
    Generates simulated market data events.

    Args:
        symbols: List of stock symbols.
        num_events: Number of events to generate.

    Yields:
        MarketEvent: A market data event.
    """
    for _ in range(num_events):
        event = MarketEvent(
            symbol=random.choice(symbols),
            price=round(random.uniform(100, 200), 2),
            volume=random.randint(1, 1000),
            timestamp=datetime.now()
        )
        yield event
        sleep(0.1) # Add a small delay to simulate real-time data flow

def publish_market_data(producer: KafkaProducer, symbols: List[str], num_events: int) -> None:
    """
    Publishes market data events to a Kafka topic.

    Args:
        producer: Kafka producer instance.
        symbols: List of stock symbols.
        num_events: Number of events to generate and send.
    """
    for event in market_data_generator(symbols, num_events):
        try:
            # Use the to_dict method from MarketEvent
            producer.send(MARKET_EVENTS_TOPIC, value=event.to_dict())
            print(f"Sent: {event}")  # Keep printing, but use the event object.
        except Exception as e:
            print(f"Error sending event: {e}")
            break # Stop sending if there's an error.  Consider more sophisticated error handling.
    producer.flush() # Ensure all pending messages are delivered

def create_kafka_producer() -> KafkaProducer:
    """
    Creates and returns a Kafka producer instance.
    """
    return KafkaProducer(
        bootstrap_servers=KAFKA_BROKERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        # Add other serializers if needed (e.g., for different data formats)
    )

if __name__ == "__main__":
    symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    num_events = 20  # Number of events to send
    producer = create_kafka_producer()
    publish_market_data(producer, symbols, num_events)
    producer.close()
    print("Producer finished.")