"""Minimal test to ensure package importability."""

import importlib


def test_import() -> None:
    assert importlib.import_module('trading_system') is not None
