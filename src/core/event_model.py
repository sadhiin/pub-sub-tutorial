# trading_system/src/core/event_model.py
# Defines the structure of events in the trading system
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict

@dataclass
class MarketEvent:
    """
    Represents a market data event.
    """
    symbol: str
    price: float
    volume: int
    timestamp: datetime

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the MarketEvent to a dictionary.  Useful for serialization.
        """
        return {
            "symbol": self.symbol,
            "price": self.price,
            "volume": self.volume,
            "timestamp": self.timestamp.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'MarketEvent':
        """
        Create a MarketEvent from a dictionary.  Useful for deserialization.
        """
        return cls(
            symbol=data["symbol"],
            price=data["price"],
            volume=data["volume"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
        )