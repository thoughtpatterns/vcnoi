from typing import final, override

from manim import Circumscribe, Create, FadeIn, FadeOut, Restore, Uncreate, Transform

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
        self.play(Create(emph), wuf(44.4))

        # Graphic artists working for Muhammad Speaks [...] the different perpetrators of oppression...
        skull = image("skull.png")
        self.play(FadeOut(wihdfm), FadeOut(emph), FadeIn(skull), wuf(54.4))

        # ...such as the police, courts, prisons, and laws [...] was not the enforcement of justice...
        scales = image("scales.png")
        self.play(FadeOut(skull), FadeIn(scales), wuf(65.2))

        # ...but the continuation of black subjugation [...]  mass incarceration goes beyond the jails.
        jails = image("jails.png")
        self.play(FadeOut(scales), FadeIn(jails), wuf(74.3))

        # Instead, it is a direct attack [...] enlightenment and empowerment through Islam can counter.
        chain = image("chain.png")
        self.play(FadeOut(jails), FadeIn(chain), wuf(84.7))

        # Among many examples, in the section of "Prison News in Black," [...] to recognize his innocence.
        news = image("news.png")
        self.play(FadeOut(chain), FadeIn(news), wuf(100.4))

        # A graphic accompanying his first-person account [...] its star-and-crescent moon logo.
        frame.save_state()
        emph = emphf(1183, 1433, 480, 124.5)
        self.play(
            frame.animate.move_to((emph.frame_x, emph.frame_y, 0)).set(width=emph.frame_width * 1.625),
            Create(emph),
            wuf(115.9),
        )

        # The flag also refers to the NOI's nationhood [...] "and helped them succeed in life".
        flag = image("flag.png")
        self.play(
            news.animate.move_to((-1.625, 0, 0)),
            FadeIn(flag.scale(0.4875).move_to((4.5, 0.5, 0))),
            emph.animate.move_to((-1.625, 0, 0)),
            wuf(128.2),
        )

        # In this graphic, the imprisoned man [...] which become a path to freedom itself.
        self.play(
            frame.animate.move_to((emph.frame_x, emph.frame_y, 0)).set(width=emph.frame_width * 1.5),
            news.animate.move_to((0, 0, 0)),
            flag.animate.move_to((7.5, 0.5, 0)),  # Move offscreen.
            Transform(emph, emphf(713, 650, 482.5, 209.5)),
            wuf(130.3),
        )
        self.remove(flag)
        self.play(wuf(147.5))

        # In other words [...] the United States' white supremacist legal system.
        self.play(Uncreate(emph), wuf(163.0))

        # By reframing confinement as an opportunity [...] Elijah Muhammad promises a path to reclaim it.
        emancipation = image("emancipation.png")
        self.play(Restore(frame), FadeOut(news), FadeIn(emancipation), wuf(186.4))

        # By positioning Islam [...] a symbol of sovereignty rather than subjugation.
        news_zoom = image("news-zoom.png")
        self.play(
            emancipation.animate.scale(0.825).move_to((-3.725, 0, 0)),
            FadeIn(news_zoom.scale(0.75).move_to((3.125, 0, 0))),
            wuf(203.7),
        )
        self.play(FadeOut(emancipation), FadeOut(news_zoom), wuf(205.7))


if __name__ == "__main__":
    PrisonNewsInBlack.run()
