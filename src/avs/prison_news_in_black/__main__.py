from typing import final, override

from manim import Circumscribe, Create, FadeIn, FadeOut, Restore, Uncreate

from lib import MetaScene, Paths, Pixels, Wuf, emphf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class PrisonNewsInBlack(MetaScene):
    voiceover = asset("voiceover.wav")
    config = {"pixel_height": 2160, "pixel_width": 3840, "frame_rate": 60}

    @override
    def scene(self, wuf: Wuf) -> None:
        frame = self.camera.frame

        # The NOI and the U.S. Penal System's fraught relationship [...] Black and Muslim identities behind bars.
        philly = image("philly.png")
        self.play(FadeIn(philly), wuf(24.0))

        # As the scholar Edward Curtis IV notes [...] included in a section entitled...
        wihdfm = image("wihdfm.png")
        self.play(FadeOut(philly), FadeIn(wihdfm), wuf(39.5))

        # ..."What Islam Has Done For Me" in the NOI's newspaper, Muhammad Speaks.
        emph = emphf(164, 1466, -10, 919)
        self.play(Circumscribe(emph.frame, color=emph.frame.stroke_color), wuf(44.4))

        # Graphic artists working for Muhammad Speaks [...] enlightenment and empowerment through Islam can counter.
        skull = image("skull.png")
        self.play(FadeOut(wihdfm), FadeIn(skull), wuf(84.8))

        # Among many examples, in the section of "Prison News in Black," [...] to recognize his innocence.
        news = image("news.png")
        self.play(FadeOut(skull), FadeIn(news), wuf(100.4))

        # A graphic accompanying his first-person account [...] which become a path to freedom itself.
        frame.save_state()
        emph = emphf(1183, 1433, 480, 124.5)
        self.play(
            frame.animate.move_to((emph.frame_x, emph.frame_y, 0)).set(width=emph.frame_width * 1.625),
            Create(emph),
            wuf(147.5),
        )

        # In other words [...] the United States' white supremacist legal system.
        self.play(Restore(frame), Uncreate(emph), wuf(163.0))

        # By reframing confinement as an opportunity [...] Elijah Muhammad promises a path to reclaim it.
        emancipation = image("emancipation.png")
        self.play(FadeOut(news), FadeIn(emancipation), wuf(186.4))

        # By positioning Islam [...] a symbol of sovereignty rather than subjugation.
        self.play(
            emancipation.animate.scale(0.825).move_to((-3.425, 0, 0)),
            FadeIn(news.scale(0.75).move_to((3.425, 0, 0))),
            wuf(203.7),
        )
        self.play(FadeOut(emancipation), FadeOut(news), wuf(205.7))


if __name__ == "__main__":
    PrisonNewsInBlack.run()
