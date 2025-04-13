from src.application_events.poducer import make_data_generator

from src.bocker_events.producer import produce_market_events
from src.models.schemas import MarketEvent
from datetime import datetime


def run_producer():
    symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    events = make_data_generator(symbols, 10)

    # Produce the market events to Kafka
    produce_market_events(events)
    print("Market events produced successfully.")

if __name__ == "__main__":
    run_producer()
# Compare this snippet from src/models/schemas.py: