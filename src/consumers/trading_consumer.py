# Consumes market data events from Kafka and applies a trading strategy
import json
from typing import Callable
from kafka import KafkaConsumer
from src.core.event_model import MarketEvent
from src.config.settings import KAFKA_BROKERS, MARKET_EVENTS_TOPIC, DEFAULT_STRATEGY_THRESHOLD
from src.processing.strategies import SimpleTradingStrategy
from src.utils.serializers import market_event_deserializer

def create_kafka_consumer() -> KafkaConsumer:
    """
    Creates and returns a Kafka consumer instance.
    """
    return KafkaConsumer(
        MARKET_EVENTS_TOPIC,
        bootstrap_servers=KAFKA_BROKERS,
        # Important:  Deserialize the JSON back into a dictionary, then use from_dict
        # value_deserializer=lambda m: MarketEvent.from_dict(json.loads(m['value'].decode('utf-8'))),
        value_deserializer=lambda m: market_event_deserializer(m),
        # Alternatively, you can use a custom deserializer if needed
        auto_offset_reset='earliest',  # Start consuming from the beginning
        enable_auto_commit=True # Automatically commit offsets
    )

def process_market_events(consumer: KafkaConsumer, strategy: Callable[[MarketEvent], None]) -> None:
    """
    Consumes market data events from Kafka and processes them using a trading strategy.

    Args:
        consumer: Kafka consumer instance.
        strategy: A function that takes a MarketEvent and performs a trading action.
    """
    for message in consumer:
        event = message.value
        strategy(event) # Call the strategy function

def run_consumer():
    """
    Main function to run the consumer.
    """
    consumer = create_kafka_consumer()
    strategy = SimpleTradingStrategy(threshold=DEFAULT_STRATEGY_THRESHOLD).process_event # Get the process_event method
    print("Consumer started.  Waiting for events...")
    try:
        process_market_events(consumer, strategy)
    except KeyboardInterrupt:
        print("Consumer stopped by user.")
    finally:
        consumer.close() # Close the consumer to free up resources.
    print("Consumer finished.")

if __name__ == "__main__":
    run_consumer()