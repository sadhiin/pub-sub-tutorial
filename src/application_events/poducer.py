import random
from datetime import datetime
from src.models.schemas import MarketEvent

def make_data_generator(symbols, num_events):
    for _ in range(num_events):
        event = MarketEvent(
            symbol=random.choice(symbols),
            price=round(random.uniform(100, 200), 2),
            volume=random.randint(1, 1000),
            timestamp=datetime.now()
        )
        yield event

symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
events = make_data_generator(symbols, 10)
        