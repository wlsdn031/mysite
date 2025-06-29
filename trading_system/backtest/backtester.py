"""Backtesting utilities for strategy evaluation."""

from typing import Iterable, Any

from ..signals.base import Signal


class Backtester:
    """Runs historical simulations given a set of signals."""

    def __init__(self, signals: Iterable[Signal]) -> None:
        self.signals = list(signals)

    def run(self, data: Any) -> dict:
        """Run the backtest and return performance metrics."""
        raise NotImplementedError
