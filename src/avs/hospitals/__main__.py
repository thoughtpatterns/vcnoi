from functools import partial
from typing import final, override

from manim import Circumscribe, Create, FadeIn, FadeOut, Transform, Uncreate

from lib import MetaScene, Paths, Pixels, Wuf, emphf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class Hospitals(MetaScene):
    voiceover = asset("voiceover.wav")
    config = {"pixel_height": 2160, "pixel_width": 3840, "frame_rate": 60}

    @override
    def scene(self, wuf: Wuf) -> None:
        # In July 1970, a cartoon by NOI artist...
        hospitals = image("hospitals.png")
        self.play(FadeIn(hospitals), wuf(3.9))

        # ...Gerald 2X [...] dedicated to explaining...
        emph = emphf(44, 451, 433.5, 756)
        self.play(Circumscribe(emph.frame, color=emph.frame.stroke_color), wuf(14.3))

        # "...The Messenger Muhammad's Program."
        emph = emphf(86, 1323, -7.5, 954)
        self.play(Create(emph), wuf(17.0))

        # Entitled "Hospitals...," this pictorial spread [...] to diner foods under its control.
        transformf = partial(Transform, emph)
        self.play(transformf(emphf(164, 1327, -1.5, 814)), wuf(26.2))

        # In the top panel, a heavy-set Black man [...] Below appears an exclamation uttered by the white man...
        self.play(transformf(emphf(872, 1316, -16, 303)), wuf(43.0))

        # "Why do you say we need more hospitals? We have plenty hospitals..." [...] the pronouns "we" and "you."
        self.play(transformf(emphf(92, 1316, -16, -56)), wuf(61.5))

        # Moving down, in the lower panel [...] the two seated men...
        self.play(transformf(emphf(999, 1390, -53, -567.5)), wuf(86.4))

        # ...include one, on the right [...] to signal his physical discomfort.
        self.play(transformf(emphf(491, 354, 170, -586.5)), wuf(97.1))

        # Similarly, the waiter's skin [...] with a large bandage appearing on his lower back.
        self.play(transformf(emphf(399, 484, -445, -367.5)), wuf(104.2))

        # All three Black men are shown overweight [...] as the caption at the bottom notes...
        self.play(transformf(emphf(718, 1030, -172, -527)), wuf(111.0))

        # "Healthy as people are nowadays I can't see the necessity of a hospital."
        self.play(transformf(emphf(41, 1220, -89, -1046.5)), wuf(115.8))

        # The superposition of these two images [...] especially as expounded in...
        self.play(Uncreate(emph), wuf(135.7))

        # ...his How to Eat to Live [...] as spread through America's white-owned fast-food industry.
        eat = image("eat.png")
        self.play(FadeOut(hospitals), FadeIn(eat), wuf(176.0))

        # By avoiding such establishments [...] as a form of both physical and spiritual salvation.
        earth = image("earth.png")
        self.play(FadeOut(eat), FadeIn(earth), wuf(205.6))
        self.play(FadeOut(earth), wuf(207.6))


if __name__ == "__main__":
    Hospitals.run()
