from functools import partial
from typing import final, override

from manim import Create, FadeIn, FadeOut, Transform, Uncreate

from lib import MetaScene, Paths, Pixels, Wuf, emphf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class OnDangerousGround(MetaScene):
    voiceover = asset("voiceover.wav")
    intro = False
    # config = {"pixel_height": 1080, "pixel_width": 1920, "frame_rate": 60}

    @override
    def scene(self, wuf: Wuf) -> None:
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
        self.play(transformf(emphf(693, 840, 902.5, -14.5)), wuf(68.4))

        # On the left [...]
        self.play(transformf(emphf(812, 609, -1022, 63)), wuf(77.6))

        # Inside the widening chasm [...]
        self.play(transformf(emphf(930, 725, -47, -467)), wuf(122.9))

        # This critique of King [...]
        self.play(Uncreate(emph), wuf(199.3))
        self.play(FadeOut(on_dangerous_ground), wuf(201.3))


if __name__ == "__main__":
    OnDangerousGround.run()
