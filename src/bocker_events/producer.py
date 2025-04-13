from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)

def produce_market_events(events):
    """
    Produce market events to the Kafka topic 'market_events'.
    """
    for event in events:
        producer.sent('market_events', event)