from collections.abc import Callable
from functools import partial
from types import SimpleNamespace
from typing import final

from manim import ImageMobject


@final
class Pixels(SimpleNamespace):  # noqa: D101
    to_units: Callable[[float], float] = lambda x: x / 270  # 2160 / 8 (Manim unit frame height) == 270.
    """Translate pixels to Manim units.

    This method assumes the passed pixel count corresponds to a 4K image, to prevent enlargements among elements if
    rendered at lower resolutions.
    """

    image: Callable[[str], ImageMobject] = partial(ImageMobject, scale_to_resolution=2160)
    """Simplify creation of `ImageMobject`."""

    imagef: Callable[[Callable[[str], str]], Callable[[str], ImageMobject]] = lambda f: lambda x: Pixels.image(f(x))
    """Simplify calls of form `f = lambda x: Pixels.image(asset(x))`."""


__all__ = ["Pixels"]
