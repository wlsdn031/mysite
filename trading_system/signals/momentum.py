"""Momentum and breakout style signals."""

from typing import Any

from .base import Signal


def momentum_signal(data: Any, window: int = 20) -> Any:
    """Simple momentum signal placeholder."""
    raise NotImplementedError


class BreakoutSignal(Signal):
    """Price breakout based entry signal."""

    def __init__(self, lookback: int = 20) -> None:
        self.lookback = lookback

    def generate(self, data: Any) -> Any:
        return momentum_signal(data, window=self.lookback)
