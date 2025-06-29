"""Abstraction over brokerage or exchange APIs."""

from typing import Any


class BrokerAPI:
    """Simple wrapper that should encapsulate REST or SDK calls."""

    def __init__(self, token: str) -> None:
        self.token = token

    def place_order(self, symbol: str, qty: float, side: str) -> Any:
        """Send an order to the broker/exchange."""
        raise NotImplementedError

    def fetch_positions(self) -> Any:
        """Retrieve current open positions."""
        raise NotImplementedError
