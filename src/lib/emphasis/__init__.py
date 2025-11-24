from collections.abc import Callable
from typing import Any, final

from manim import (
    BLACK,
    RED_B,
    Create,
    Difference,
    Rectangle,
    Uncreate,
    VGroup,
    config,
    override_animation,
)

from lib.pixels import Pixels
from lib.stroke import Stroke


# If an `Emphasis` is clipped at the edge of the video frame, a `Transform` animation must "flip" the outer frame: this
# should be avoided, where possible.
@final
class Emphasis(VGroup):
    """A black-bordered red frame, and a transparent fill which extends from the frame to the scene borders.

    Parameters
    ----------
    height
        The vertical height of the frame.
    width
        The horizontal width of the frame.
    x
        The x coordinate of the center of the frame.
    y
        The y coordinate of the center of the frame.

    """

    def __init__(self, height: float, width: float, x: float, y: float) -> None:  # noqa: D107
        self.frame_height: float = height
        self.frame_width: float = width
        self.frame_x: float = x
        self.frame_y: float = y

        fill_stroke = Stroke(RED_B, 4)
        border_stroke = Stroke(BLACK, 8)

        subject = Rectangle(height=config.frame_height, width=config.frame_width)

        clip = Rectangle(
            height=height + Stroke.to_units(border_stroke.width),
            width=width + Stroke.to_units(border_stroke.width),
            stroke_color=fill_stroke.color,
            stroke_width=fill_stroke.width,
            background_stroke_color=border_stroke.color,
            background_stroke_width=border_stroke.width,
        ).move_to((x, y, 0))

        super().__init__(
            Difference(
                subject,
                clip,
                fill_color=BLACK,
                fill_opacity=0.3,
                stroke_opacity=0.0,
                background_stroke_opacity=0.0,
            ),
            clip,
        )

    @property
    def fill(self) -> Difference:
        """The fill of the `VGroup`."""
        return self[0]

    @fill.setter
    def fill(self, value: Difference) -> None:
        self[0] = value

    @property
    def frame(self) -> Rectangle:
        """The frame of the `VGroup`."""
        return self[1]

    @frame.setter
    def frame(self, value: Rectangle) -> None:
        self[1] = value

    @override_animation(Create)
    def _create_override(self, **kwargs: Any) -> list[Create]:  # pyright: ignore[reportUnusedFunction]
        return [Create(s, **kwargs) for s in self]

    @override_animation(Uncreate)
    def _uncreate_override(self, **kwargs: Any) -> list[Uncreate]:  # pyright: ignore[reportUnusedFunction]
        return [Uncreate(s, **kwargs) for s in self]


emphf: Callable[[float, float, float, float], Emphasis] = lambda h, w, x, y: Emphasis(
    height=Pixels.to_units(h),
    width=Pixels.to_units(w),
    x=Pixels.to_units(x),
    y=Pixels.to_units(y),
)
"""Create `Emphasis` objects with pixel values."""


__all__ = ["Emphasis", "emphf"]
