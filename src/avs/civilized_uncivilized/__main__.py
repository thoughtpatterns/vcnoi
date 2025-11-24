from functools import partial
from typing import final, override

from manim import Create, FadeIn, FadeOut, Restore, Transform, Uncreate

from lib import MetaScene, Paths, Pixels, Wuf, emphf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class CivilizedUncivilized(MetaScene):
    voiceover = asset("voiceover.wav")
    config = {"pixel_height": 1080, "pixel_width": 1920, "frame_rate": 60}

    @override
    def scene(self, wuf: Wuf) -> None:
        frame = self.camera.frame

        # A two-page spread appeared in the August 21, 1970 copy of Muhammad Speaks. Across four registers...
        civilized = image("civilized.png")
        self.play(FadeIn(civilized), wuf(8.9))

        # NOI artist Eugene Majied states that he has drawn [...] clearly noted in the lower right.
        frame.save_state()
        emph = emphf(85, 378, 1268, -940.5)

        self.play(
            frame.animate.move_to((emph.frame_x, emph.frame_y, 0)).set(width=emph.frame_width * 4),
            Create(emph),
            wuf(18.2),
        )

        # The composition aims to encapsulate [...] the wearing of proper Muslim vestment.
        self.play(Restore(frame), Uncreate(emph), wuf(27.2))

        # On the right page, a thin vertical line separates two panels...
        emph = emphf(1670, 1461, 756.5, 208)
        self.play(Create(emph), wuf(32.9))

        # ...each labeled "Civilized" and "Uncivilized."
        transformf = partial(Transform, emph)
        self.play(transformf(emphf(112, 1209, 785.5, -761)), wuf(37.5))

        # The uncivilized half, on the right...
        self.play(transformf(emphf(1648, 754, 1104, 197)), wuf(40.6))

        # ...depicts three individuals in the foreground [...] "Soul Style" movements.
        self.play(transformf(emphf(992, 754, 1104, -43)), wuf(56.6))

        # On the civilized side, to the left...
        self.play(transformf(emphf(1648, 754, 399, 197)), wuf(59.1))

        # ...a group of men wear long robes, shalwars, turbans, and fezzes, [...] especially in an African context.
        self.play(transformf(emphf(1017, 754, 399, 49.5)), wuf(71.8))

        # Zooming in a bit further, these men also appear racially diverse, [...] black bodies standing on the right.
        self.play(transformf(emphf(190, 754, 399, 463)), wuf(82.5))

        # Moving over to the left page of the spread, a question is posed to the viewers and readers...
        self.play(transformf(emphf(2087, 1513, -783.5, -26.5)), wuf(89.2))

        # "What is beautiful about wearing long hair? I can see nothing about it but savagery!"
        self.play(transformf(emphf(618, 759, -784.5, 592)), wuf(98.3))

        # The query hovers between a white and black man. Both men have long, bushy beards and wild, disheveled hair.
        self.play(transformf(emphf(618, 1427, -778.5, 592)), wuf(107.7))

        # The black man on the right seems to have locked the white man in his gaze, as if to follow or even obey him.
        self.play(transformf(emphf(618, 357, -243.5, 592)), wuf(116.0))

        # In the final box of this spread, the text exclaims...
        self.play(transformf(emphf(1347, 1501, -786.5, -392.5)), wuf(120.5))

        # ..."You are following them into SAVAGERY!"
        self.play(transformf(emphf(318, 1168, -759, 71)), wuf(125.8))

        # Here, a group of black individuals run behind...
        self.play(transformf(emphf(803, 840, -1052, -366.5)), wuf(127.9))

        # ...a shaggy white savage man and his companion downwards, into the darkness.
        self.play(transformf(emphf(421, 410, -455, -700.5)), wuf(134.1))

        # Bats fly out of a concavity to signal the feral nature of the white cavemen.
        self.play(transformf(emphf(172, 299, -266.5, -514)), wuf(140.5))

        # In this graphic by Eugene Majied [...] "visibly Muslim" in the public sphere.
        self.play(Uncreate(emph), wuf(196.2))
        self.play(FadeOut(civilized), wuf(198.2))


if __name__ == "__main__":
    CivilizedUncivilized.run()
