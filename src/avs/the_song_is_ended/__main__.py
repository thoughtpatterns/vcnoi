from functools import partial
from typing import final, override

from manim import Create, FadeIn, FadeOut, Transform, Uncreate

from lib import MetaScene, Paths, Pixels, Wuf, emphf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class TheSongIsEnded(MetaScene):
    voiceover = asset("voiceover.wav")
    intro = False
    # config = {"pixel_height": 1080, "pixel_width": 1920, "frame_rate": 60}

    @override
    def scene(self, wuf: Wuf) -> None:
        # Decades before #blacklivesmatter [...]
        black_lives_matter = image("black-lives-matter.png")
        self.play(FadeIn(black_lives_matter), wuf(6.4))

        # ...exposing police violence...
        imagef = lambda x: image(x).scale(0.9)
        handle_the_scales = imagef("handle-the-scales.png").move_to((-3, 0, 0))
        self.play(FadeOut(black_lives_matter), FadeIn(handle_the_scales), wuf(7.6))

        # ...and mass incerceration [...]
        angela_davis = imagef("angela-davis.png").move_to((3.25, 0, 0))
        self.play(FadeIn(angela_davis), wuf(45.0))

        # For example, the April 10, 1964 issue of the paper [...]
        the_song_is_ended = image("the-song-is-ended.png")
        self.play(FadeOut(handle_the_scales), FadeOut(angela_davis), FadeIn(the_song_is_ended), wuf(53.8))

        # Mirroring one another [...]
        emph = emphf(541, 2101, 63.5, -776.5)
        self.play(Create(emph), wuf(62.3))

        # In the first frame on the left...
        transformf = partial(Transform, emph)
        self.play(transformf(emphf(2005, 1037, -598.5, -49.5)), wuf(73.8))

        # The Klansman's chest [...]
        self.play(transformf(emphf(264, 313, -764.5, 216)), wuf(80.2))

        # He is accompanied by another Klansman...
        self.play(transformf(emphf(808, 176, -1036, 310)), wuf(82.7))

        # ...whose hand is gripping the leashes of two bloodhounds [...]
        self.play(transformf(emphf(476, 581, -772.5, -635)), wuf(88.9))

        # In the distance [...]
        self.play(transformf(emphf(473, 204, -186, 502.5)), wuf(97.2))

        # Here, Irving Berlin's 1927 hit [...]
        self.play(Uncreate(emph), wuf(110.6))

        # In the second frame on the right...
        emph = emphf(1860, 1225, 496.5, -127)
        self.play(Create(emph), wuf(121.1))

        # ...while his uniform is emblazoned [...]
        transformf = partial(Transform, emph)
        self.play(transformf(emphf(275, 312, 317, 266.5)), wuf(126.2))

        # Behind him another officer smiles ear-to-ear...
        self.play(transformf(emphf(699, 375, 923.5, 333.5)), wuf(129.5))

        # ...as he grips the leash [...]
        self.play(transformf(emphf(610, 442, 865, -230)), wuf(135.2))

        # The bloodhounds in the first frame [...]
        self.play(Uncreate(emph), wuf(190.0))
        self.play(FadeOut(the_song_is_ended), wuf(192.0))

if __name__ == "__main__":
    TheSongIsEnded.run()
