"""Core strategy workflow handling signals and risk modules."""

from dataclasses import dataclass
from typing import Any, Iterable

from ..signals.base import Signal


@dataclass
class Position:
    symbol: str
    size: float
    entry_price: float


class StrategyEngine:
    """Integrates market gate, signal evaluation and order handling."""

    def __init__(self, signals: Iterable[Signal]) -> None:
        self.signals = list(signals)
        self.positions: list[Position] = []

    def on_data(self, data: Any) -> None:
        """Process new market data and update positions."""
        for signal in self.signals:
            signal.generate(data)
        # Placeholder: implement order logic here
        raise NotImplementedError
