# Defines trading strategies for processing market events
from src.core.event_model import MarketEvent

class SimpleTradingStrategy:
    """
    A simple trading strategy that buys a stock if its price falls below a threshold.
    """
    def __init__(self, threshold: float):
        """
        Initializes the strategy with a price threshold.

        Args:
            threshold: The price threshold below which to buy.
        """
        self.threshold = threshold

    def process_event(self, event: MarketEvent) -> None:
        """
        Processes a market event and decides whether to buy or not.

        Args:
            event: The market event to process.
        """
        if event.price < self.threshold:
            print(f"BUY: {event.symbol} at {event.price} (Volume: {event.volume}, Timestamp: {event.timestamp})")
        else:
            print(f"Price of {event.symbol} is above threshold ({event.price}).  No action.")