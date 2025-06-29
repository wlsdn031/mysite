"""Data ingestion and preprocessing utilities.

This module handles data collection from various sources, including
price history, indicators, and external metrics such as VIX or ATR.
Future versions may expand to crypto exchanges.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class DataConfig:
    """Configuration for data pipeline."""
    source: str
    timeframe: str
    symbols: list[str]


def fetch_data(config: DataConfig) -> Any:
    """Fetch raw data according to the configuration.

    Placeholder function to be implemented with real data sources.
    """
    raise NotImplementedError


def build_dataset(raw: Any) -> Any:
    """Transform raw data into model-ready dataset."""
    raise NotImplementedError
