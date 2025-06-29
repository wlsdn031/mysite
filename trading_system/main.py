"""Entry point for running strategy components from the command line."""

from .strategy.engine import StrategyEngine
from .signals.momentum import BreakoutSignal


def main() -> None:
    engine = StrategyEngine(signals=[BreakoutSignal()])
    # This would normally initialize data feeds and start the loop
    raise NotImplementedError


if __name__ == "__main__":
    main()
