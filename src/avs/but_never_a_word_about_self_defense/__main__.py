from functools import partial
from typing import final, override

from manim import Create, FadeIn, FadeOut, Group, Restore, Transform

from lib import MetaScene, Paths, Pixels, Wuf, emphf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class ButNeverAWordAboutSelfDefense(MetaScene):
    voiceover = asset("voiceover.wav")
    # config = {"pixel_height": 1080, "pixel_width": 1920, "frame_rate": 60}

    @override
    def scene(self, wuf: Wuf) -> None:
        pass


if __name__ == "__main__":
    ButNeverAWordAboutSelfDefense.run()
