from functools import partial
from typing import final, override

from manim import (
    LIGHTER_GREY,
    ORIGIN,
    RED_B,
    WHITE,
    Circle,
    Create,
    Difference,
    FadeOut,
    Line,
    Scene,
    Star,
    Text,
    Transform,
    VGroup,
    register_font,
)
from numpy import pi

from lib.epicycle import Epicycle
from lib.paths import Paths
from lib.stroke import Stroke

asset = partial(Paths.asset, __file__)


def intro(self: Scene) -> None:
    """Render the project's video intro.

    1. An array of circles and lines are created,
    2. which draw a crescent via `Epicycle`,
    3. then the circles expand to form one large circle, which borders the crescent, and the lines transform into a
       star, to form the Flag of Islam.
    4. The shapes are filled,
    5. and the name of the project is drawn below.
    """
    # <*> HACK: Among all tested powers of 2, `nterms = 128` was the largest which gave a good trace of the `intro()`
    # crescent at `-qk`, did not cause the trace to vanish on completion, and indeed completed the path rather than
    # stopping short.

    # <**> HACK: Without `--disable_caching`, the trail will vanish after this animation, which requires two passes to
    # fix. With it, however, the animation misses a cycle of trace movement, so we compensate with the addition of
    # a small amount of extra time. For now, `(nterms + 1) / nterms / speed`, rather than `1 / speed`, works for
    # `nterms == 128`, but other values work: this is simply the pair of largest `nterms` and closest `run_time`
    # value to `1 / speed` tested, which did not affect the shape of the portrait in `intro()` at `-qk`, either
    # with dull corners, or a failure to complete the path. The downside for this workaround in intro is quite
    # imperceptible, as we only see the trace travel ahead of the dot by one frame.

    nterms: float = 128  # See <*>.
    speed: float = 0.5

    crescent = Epicycle(
        obj=Difference(Circle(radius=2), Circle(radius=1.75).set_x(-0.5)),
        nterms=nterms,
        speed=speed,
        run_time=(nterms + 1) / (nterms * speed),  # See <**>.
        circle_stroke=Stroke(RED_B, 2),
        dot_stroke=Stroke(LIGHTER_GREY, 0.05),
        line_stroke=Stroke(LIGHTER_GREY, 2),
        trail_stroke=Stroke(WHITE, 4),
    )

    self.play(Create(crescent.trace, run_time=1), Create(crescent.dot, run_time=0.1))
    self.add_sound(asset("music.wav"))
    self.add(crescent.trail)

    crescent.play(self)
    self.wait(0.1, frozen_frame=True)

    border = Circle(
        radius=3,
        stroke_color=crescent.circle_stroke.color,
        stroke_width=4,
        z_index=-1,
    )

    star = Star(
        n=5,
        start_angle=-pi,
        stroke_color=crescent.trail_stroke.color,
        stroke_width=crescent.trail_stroke.width,
    ).set_x(-1)

    unified_line = Line(
        start=ORIGIN,
        end=(max(line.get_x() for line, _ in crescent.trace), 0, 0),
        stroke_color=crescent.line_stroke.color,
        stroke_width=crescent.line_stroke.width,
    )

    circles: dict[str, VGroup] = {"small": VGroup(), "large": VGroup()}

    for _, circle in crescent.trace:
        key = "small" if circle.width < crescent.dot.width else "large"
        circles[key] += circle

    self.remove(crescent.trace)

    self.play(
        *[Transform(circle, border) for circle in circles["large"]],
        *[circle.animate.match_x(crescent.dot) for circle in circles["small"]],
        Transform(unified_line, star),
    )

    self.add(border)
    self.remove(*circles["small"], *circles["large"])
    self.wait(0.1, frozen_frame=True)

    with register_font(Paths.common / "CMUSerif.ttf"):
        text = Text("The Visual Culture of the Nation of Islam", font="CMU Serif").set_y(-3.5)

    self.play(
        FadeOut(crescent.dot),
        Create(text),
        crescent.trail.animate.set_fill(crescent.trail.stroke_color, opacity=1),
        star.animate.set_fill(star.stroke_color, opacity=1),
        border.animate.set_fill(border.stroke_color, opacity=1),
    )

    self.wait(1, frozen_frame=True)
    self.play(FadeOut(*self.mobjects))  # pyright: ignore[reportAttributeAccessIssue]
    self.clear()


# Provided to render the intro standalone if necessary.
@final
class Intro(Scene):  # noqa: D101
    @override
    def construct(self) -> None:
        intro(self)


__all__ = ["Intro", "intro"]
