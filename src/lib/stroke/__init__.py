from dataclasses import dataclass
from typing import final

from manim import ManimColor


@final
@dataclass
class Stroke:
    """Common interface to managing stroke color/width."""

    color: ManimColor
    width: float

    @staticmethod
    def to_units(width: float) -> float:
        """Translate stroke width to Manim units."""
        return width / 100


__all__ = ["Stroke"]
