from kafka import KafkaConsumer
import json
from src.models.schemas import MarketEvent

consumer = KafkaConsumer(
    "market_events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="market_events_group",
    value_deserializer= lambda m: MarketEvent(**json.loads(m.decode('utf-8')))
    consumer_timeout_ms=1000,
)


for message in consumer:
    event = message.value
    print(f"Received event: {event.symbol} at {event.price} with volume {event.volume}")