from typing import final

from manim import ORIGIN, Circle, Dot, Line, Mobject, MoveAlongPath, Scene, TracedPath, VGroup, VMobject, linear
from numpy import abs as np_abs
from numpy import array, complex128, fft, float64, imag, linspace, pi, real

from lib.stroke import Stroke


@final
class Epicycle:
    """Construct FT terms for an epicycle animation, given a VMobject, to be played via `play()`.

    Parameters
    ----------
    obj
        The VMobject to perform the epicycle animation on.
    nterms
        The number of FT terms to calculate for the epicycle animation.
    speed
        Generally, the inverse of `run_time`; used for the updater in `play()`. See `intro()` in `lib.intro` for
        information on some bugs which arise if `speed == 1 / run_time`.
    run_time
        The duration of the epicycle animation.
    line_stroke
        The stroke of the lines of `.trace` which follow the path of `.dot`.
    circle_stroke
        The stroke of the circles of `.trace` which follow the path of `.dot`.
    dot_stroke
        The stroke of `.dot`, which follows the path of `.obj`.
    trail_stroke
        The stroke of `.trail`, which traces the path of `.dot`.

    """

    def __init__(  # noqa: PLR0913
        self,
        obj: VMobject,
        nterms: int,
        speed: float,
        run_time: float,
        line_stroke: Stroke,
        circle_stroke: Stroke,
        dot_stroke: Stroke,
        trail_stroke: Stroke,
    ) -> None:
        """Generate epicycle path objects for `obj`.

        We calculate the FT coefficient & frequency vectors, the line & circle epicycle trace, a dot to follow the
        trace, and a trail to highlight the progress of the dot.
        """
        self.obj: VMobject = obj
        self.nterms: int = nterms
        self.speed: float = speed
        self.run_time: float = run_time

        self.line_stroke: Stroke = line_stroke
        self.circle_stroke: Stroke = circle_stroke
        self.dot_stroke: Stroke = dot_stroke
        self.trail_stroke: Stroke = trail_stroke

        def ffft(path: VMobject) -> list[tuple[complex128, float64]]:
            terms = [path.point_from_proportion(p) for p in linspace(0, 1, self.nterms, endpoint=False)]
            terms = array(terms) - ORIGIN

            # Assemble list with (coefficient, frequency) pairs via FFT.
            return sorted(
                zip(
                    fft.fft(terms[:, 0] + 1j * terms[:, 1]) / self.nterms,
                    fft.fftfreq(self.nterms, 1 / self.nterms),
                    strict=True,
                ),
                key=lambda x: abs(x[1]),
            )

        def trace(fft: list[tuple[complex128, float64]]) -> VGroup:
            result = VGroup()
            center = ORIGIN

            for coeff, _ in fft:
                line = Line(
                    start=ORIGIN,
                    end=(real(coeff), imag(coeff), 0),
                    stroke_color=line_stroke.color,
                    stroke_width=line_stroke.width,
                )
                circle = Circle(
                    radius=np_abs(coeff),
                    stroke_color=circle_stroke.color,
                    stroke_width=circle_stroke.width,
                )
                result += VGroup(line, circle).shift(center)
                center = line.get_end()

            return result

        def dot(trace: VGroup) -> Dot:
            return Dot(point=trace[-1][0].get_end(), color=dot_stroke.color, radius=dot_stroke.width, z_index=1)

        # `trail` follows the path of `obj`, irrespective of the FT, which is imperceptible at high FPS, and avoids a
        # slow call to `always_redraw()` in `dot`.
        def trail(dot: Dot) -> TracedPath:
            return TracedPath(
                traced_point_func=dot.get_arc_center,
                stroke_color=trail_stroke.color,
                stroke_width=trail_stroke.width,
            )

        self.xfft: list[tuple[complex128, float64]] = ffft(self.obj)
        self.trace: VGroup = trace(self.xfft)
        self.dot: Dot = dot(self.trace)
        self.trail: TracedPath = trail(self.dot)

    def play(self, scene: Scene) -> None:
        """Render an epicycle trace of `obj`.

        Parameters
        ----------
        scene
            The scene to render the animation on, and to which `trace`, `dot`, and `trail` must be added to, prior to a
            call to this function.

        """

        def updater(trace: Mobject, dt: float) -> None:
            center = trace[0][0].get_end()

            for i, (_, freq) in enumerate(self.xfft[1:], start=1):
                trace[i][0].rotate(freq * dt * self.speed * 2 * pi, about_point=trace[i][0].get_start())
                trace[i].shift(center - trace[i][0].get_start())
                center = trace[i][0].get_end()

        _ = self.trace.add_updater(updater)
        scene.play(MoveAlongPath(mobject=self.dot, path=self.obj, run_time=self.run_time, rate_func=linear))
        _ = self.trace.remove_updater(updater)


__all__ = ["Epicycle"]
