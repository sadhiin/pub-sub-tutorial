# Configuration settings for the trading system

# Kafka broker(s)
KAFKA_BROKERS = ['localhost:9092']  # Or your Kafka broker addresses

# Kafka topic for market events
MARKET_EVENTS_TOPIC = 'market_events'

# Default trading strategy parameters
DEFAULT_STRATEGY_THRESHOLD = 150.0