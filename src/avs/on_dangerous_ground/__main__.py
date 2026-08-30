from functools import partial
from typing import final, override

from manim import (
    DOWN,
    ITALIC,
    ORIGIN,
    Create,
    FadeIn,
    FadeOut,
    Group,
    Text,
    Transform,
    Uncreate,
    config,
    register_font,
)

from lib import MetaScene, Paths, Pixels, Wuf, emphf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class OnDangerousGround(MetaScene):
    voiceover = asset("voiceover.wav")
    config = {"pixel_height": 2160, "pixel_width": 3840, "frame_rate": 60}

    @override
    def scene(self, wuf: Wuf) -> None:
        ## Preamble: it was necessary to write some code to allow the emphasis to move with the image as it slid around
        ## the video. TODO: move to a library.

        aside = 0.72  # Frame height of cartoon post-move.
        step = 918.0  # Distance to slide (in pixels, relative to 4K bounding box).
        apart = 990.0  # Distance from center.
        box = (1728.0, 1620.0)  # Bounding box for image/caption.
        gap = 54.0  # Between image and caption.

        atf = lambda x: (Pixels.to_units(x), 0, 0)
        fit = lambda m, w, h: m.scale(min(Pixels.to_units(w) / m.width, Pixels.to_units(h) / m.height, 1))
        stepf = lambda m, x: m.animate.scale_to_fit_height(config.frame_height * aside).move_to(atf(x))
        homef = lambda m: m.animate.scale_to_fit_height(config.frame_height).move_to(ORIGIN)
        emphasidef = lambda x: lambda h, w, ex, ey: emphf(h * aside, w * aside, ex * aside + x, ey * aside)

        with register_font(Paths.common / "CMUSerif.ttf"):
            captionf = lambda text: fit(Text(text=text, font_size=28, font="CMU Serif", slant=ITALIC), *box)
            photof = lambda name, caption, x: (
                Group(captionf(caption), fit(image(name), *box))
                .arrange(DOWN, buff=Pixels.to_units(gap))
                .move_to(atf(x))
                .set_z_index(1)
            )

            wc = "Wikimedia Commons."
            billy_graham = photof("billy-graham.png", f"Billy Graham preaching in 1986,\n{wc}", apart)
            goa_in_india = photof("goa-in-india.png", f"Map of India showing Goa,\n{wc}", -apart)
            albany = photof("albany.png", f"Albany Civil Rights Movement Memorial,\nAlbany, GA, {wc}", apart)

        ## End preamble.

        # In the early 1960s [...]
        brotherhood = image("brotherhood.png")
        self.play(FadeIn(brotherhood), wuf(36.3))

        # One of the most striking cartoons in the issue [...]
        on_dangerous_ground = image("on-dangerous-ground.png")
        self.play(FadeOut(brotherhood), FadeIn(on_dangerous_ground), wuf(52.0))

        # on the right, a crucifix [...]
        emph = emphf(1107, 840, 902.5, 132.5)
        self.play(Create(emph), wuf(55.4))

        # bearing a sign that reads [...]
        transformf = partial(Transform, emph)
        self.play(
            stepf(on_dangerous_ground, -step),
            transformf(emphasidef(-step)(693, 840, 902.5, -14.5)),
            FadeIn(billy_graham),
            wuf(68.4),
        )

        # On the left [...]
        self.play(
            stepf(on_dangerous_ground, step),
            transformf(emphasidef(step)(812, 609, -1022, 63)),
            FadeOut(billy_graham),
            FadeIn(goa_in_india),
            wuf(77.6),
        )

        # Inside the widening chasm [...]
        self.play(
            homef(on_dangerous_ground),
            transformf(emphf(930, 725, -47, -467)),
            FadeOut(goa_in_india),
            wuf(122.9),
        )

        # This critique of King [...]
        self.play(Uncreate(emph), wuf(161.1))

        # The image's publication coincided with Martin Luther King Jr's nonviolent direct-action campaign [...]
        self.play(stepf(on_dangerous_ground, -step), FadeIn(albany), wuf(181.1))

        # So at the very moment that King seemed to be losing political ground [...]
        self.play(homef(on_dangerous_ground), FadeOut(albany), wuf(199.3))
        self.play(FadeOut(on_dangerous_ground), wuf(201.3))


if __name__ == "__main__":
    OnDangerousGround.run()
