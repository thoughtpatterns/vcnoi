from collections.abc import Callable, Collection, Generator
from contextlib import suppress
from typing import final

from manim import FadeIn, FadeOut, FadeTransform, ImageMobject, Scene

from lib.pixels import Pixels
from lib.timestamp import Wuf

type _Fade = FadeIn | FadeTransform | FadeOut


@final
class Slides:
    """A `ImageMobject` transition generator, which loads images from a string path template.

    Parameters
    ----------
    count
        The length of the slideshow.
    template
        The path template with which to generate `ImageMobject`s, e.g., `asset("slides/{}.png")`.

    """

    def __init__(self, count: int, template: str) -> None:  # noqa: D107
        self._range: range = range(count)
        self._format: Callable[[int], str] = lambda i: template.format(i)
        self._stream: Generator[_Fade] = self._streamf()

    def __iter__(self) -> Generator[ImageMobject]:  # noqa: D105
        for i in self._range:
            (yield Pixels.image(self._format(i)))

    def _streamf(self) -> Generator[_Fade]:
        slides = iter(self)

        with suppress(StopIteration):
            yield FadeIn(current := next(slides))

            for target in slides:
                yield FadeTransform(current, target)
                current = target

            yield FadeOut(current)

    def advance(self) -> _Fade:
        """Retrieve the next transition animation."""
        return next(self._stream)


slidesf: Callable[[Scene, Wuf, str, Collection[float]], None] = lambda s, w, m, ts: (
    slides := Slides(count=len(ts) - 1, template=m),
    [s.play(slides.advance(), w(t)) for t in ts],
    None,
)[2]
"""Create a slideshow animation via parameters `(scene, wuf, template, timestamps)`."""

__all__ = ["Slides", "slidesf"]
