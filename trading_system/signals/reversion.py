"""Mean-reversion and vector based signals."""

from typing import Any

from .base import Signal


def zscore_signal(data: Any, lookback: int = 20) -> Any:
    """Compute Z-score based signal."""
    raise NotImplementedError


def vector_speed_signal(data: Any) -> Any:
    """Speed-based signal using price differentials."""
    raise NotImplementedError


class ReversionSignal(Signal):
    """Mean reversion entry/exit logic."""

    def generate(self, data: Any) -> Any:
        return zscore_signal(data)
