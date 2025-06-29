"""Signal base classes and utilities."""

from abc import ABC, abstractmethod
from typing import Any


class Signal(ABC):
    """Abstract base class for entry/exit signals."""

    @abstractmethod
    def generate(self, data: Any) -> Any:
        """Return signal values given market data."""
        raise NotImplementedError
