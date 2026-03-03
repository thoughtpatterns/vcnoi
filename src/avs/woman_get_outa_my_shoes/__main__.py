from functools import partial
from typing import final, override

from manim import Create, FadeIn, FadeOut, Restore, Transform, Uncreate

from lib import MetaScene, Paths, Pixels, Wuf, emphf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class WomanGetOutaMyShoes(MetaScene):
    voiceover = asset("voiceover.wav")
    # config = {"pixel_height": 1080, "pixel_width": 1920, "frame_rate": 60}

    @override
    def scene(self, wuf: Wuf) -> None:
        # Central to the Nation of Islam's mission was [...] including those concerned with masculinity and femininity.
        uniformity = image("uniformity.png")
        self.play(FadeIn(uniformity), wuf(37.3))

        # Fashion was reflected in the visuals [...] is parodied through a three-panel sequence.
        shoes = image("shoes.png")
        self.play(FadeOut(uniformity), FadeIn(shoes), wuf(59.3))

        # The first two panels introduce a domestic scene.
        emph = emphf(949, 1537, 8, 584.5)
        self.play(Create(emph), wuf(62.8))

        # A husband appears to surprise his wife with a pair of platform shoes, [...] to express care and indulgence.
        transformf = partial(Transform, emph)
        self.play(transformf(emphf(123, 202, -513.5, 410.5)), wuf(70.6))

        # The wife seems ecstatic as she dons the new items...
        self.play(transformf(emphf(667, 277, 618, 486.5)), wuf(74.1))

        # ...declaring that she can't wait to flaunt them in public.
        self.play(transformf(emphf(221, 437, 560, 917.5)), wuf(77.3))

        # The scene appears to be a harmless conjunction of shared passion for consumer fashion and marital affection.
        self.play(transformf(emphf(949, 1537, 8, 584.5)), wuf(84.4))

        # However, the comic takes a sharp turn [...] "Woman, get outa my shoes!"
        self.play(transformf(emphf(1180, 1537, 8, -467)), wuf(101.2))

        # Echoing Elijah Muhammad's messages [...] in this image and elsewhere...
        self.play(Uncreate(emph), wuf(140.4))

        # ...popular Black styles were frequently targeted by the NOI [...] into white-controlled consumer culture.
        emph = emphf(232, 1156, 103.5, -940)
        self.play(Create(emph), wuf(149.1))

        # Through this humorous triptych [...] the civilized Black Muslim male and female subject.
        self.play(Uncreate(emph), wuf(185.5))
        self.play(FadeOut(shoes), wuf(187.5))


if __name__ == "__main__":
    WomanGetOutaMyShoes.run()
