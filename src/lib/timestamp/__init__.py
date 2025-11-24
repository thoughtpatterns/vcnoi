from collections.abc import Callable
from dataclasses import dataclass
from functools import partial
from typing import Any, final

from manim import Wait


@final
@dataclass
class Timestamp:
    """A `float` mutability wrapper."""

    now: float = 0


class WaitUntil(Wait):
    """Wait from a `Timestamp` to a given time, then update the passed `Timestamp`.

    This replaces `Wait(b - a); Wait(c - b)` with `WaitUntil(timestamp, b); WaitUntil(timestamp, c)`.

    Parameters
    ----------
    timestamp
        A `Timestamp`, to wait from.
    until
        A `float`, to wait until.

    """

    def __init__(self, timestamp: Timestamp, until: float, **kwargs: Any) -> None:  # noqa: D107  # pyright: ignore[reportInconsistentConstructor]
        super().__init__(run_time=until - timestamp.now, **kwargs)
        timestamp.now = until


type Wuf = partial[WaitUntil]
"""The type of the return value of `wuf()`, i.e., $f : float -> WaitUntil$."""

wuf: Callable[[Timestamp], Wuf] = lambda t: partial(WaitUntil, t)
"""Simplify calls of form `f = partial(WaitUntil, t)`, to facilitate abstraction of timestamps in audiovisuals."""

__all__ = ["Timestamp", "WaitUntil", "Wuf", "wuf"]
