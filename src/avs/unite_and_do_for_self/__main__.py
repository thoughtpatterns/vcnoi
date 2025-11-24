from functools import partial
from typing import final, override

from manim import ITALIC, Circumscribe, Create, FadeIn, FadeOut, Text, Transform, Uncreate, register_font

from lib import MetaScene, Paths, Pixels, Wuf, emphf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class UniteAndDoForSelf(MetaScene):
    voiceover = asset("voiceover.wav")

    @override
    def scene(self, wuf: Wuf) -> None:
        # One of the earliest graphics to appear in Muhammad Speaks graced its interior pages...
        unite = image("unite.png")
        self.play(FadeIn(unite), wuf(5.1))

        # ...in June 1963. Entitled...
        emph = emphf(66, 328, 1306, 995)
        self.play(Create(emph), wuf(8.0))

        # "Unite and Do For Self!," it summarizes [...] The cartoon's title...
        transformf = partial(Transform, emph)
        self.play(transformf(emphf(108, 1320, -835, 905)), wuf(21.9))

        # ...in the upper left [...] This graphic was made by the famous NOI artist...
        self.play(Circumscribe(emph.frame, color=emph.frame.stroke_color), wuf(31.0))
        self.play(Uncreate(emph), wuf(35.3))

        # ...Eugene XXX, who signed his name in the lower right corner.
        emph = emphf(68, 303, 1166.5, -1005)
        self.play(Create(emph), wuf(41.6))

        # The three Xs here [...] his later Muslim name of Eugene Majied.
        self.play(transformf(emphf(42, 127, 1252.5, -1011)), wuf(50.4))
        self.play(Uncreate(emph), wuf(71.6))

        # His powerful composition aims to translate [...] a cigar smoking peddler of KKK propaganda...
        emph = emphf(1302, 578, 1197, -33)
        self.play(Create(emph), wuf(77.7))

        # ...holds a printed sign exclaiming that the Muslims are the same as the Klan.
        self.play(transformf(emphf(552, 435, 1098.5, -98)), wuf(83.6))

        # However, he is told to move on by a black man in a well-pressed suit...
        self.play(transformf(emphf(1202, 666, 684, -111)), wuf(89.4))

        # ...who goes on to say: "I've got eyes, and I can see that you're lying!"
        self.play(transformf(emphf(327, 1064, 613, 697.5)), wuf(95.6))

        # Behind them stands a large structure...
        self.play(transformf(emphf(351, 1211, 86.5, 91.5)), wuf(99.0))

        # ...embodying a Muslim record...
        record_emph = emphf(194, 278, -30, 162)
        self.play(transformf(record_emph), wuf(101.2))

        # ...of building schools, businesses, and culture.
        self.play(transformf(emphf(70, 665, -6.5, 17)), wuf(105.6))

        # Above this muscular edifice [...] emblazoned here by a crescent moon and star.
        self.play(transformf(emphf(150, 138, -68, 300)), wuf(120.2))

        # Above this flag, striated lines [...] construct a black-white binary.
        self.play(transformf(emphf(369, 780, 9, 404.5)), wuf(163.3))
        self.play(Uncreate(emph), wuf(169.8))

        # In this oppositional construct [...] These hooded men are strengthened and protected by...
        emph = emphf(869, 613, -103.5, -586.5)
        self.play(Create(emph), wuf(180.4))

        # ...security forces who wield rifles...
        self.play(transformf(emphf(840, 336, 211, -558)), wuf(183.9))

        # ...and hold attack dogs, the latter a frequent beast symbol of police brutality within NOI graphics.
        self.play(transformf(emphf(682, 506, 440, -577)), wuf(193.3))

        # While the NOI's "Muslim Record" radiates in the background...
        self.play(transformf(record_emph), wuf(197.2))

        # ...the foreground depicts the KKK's century-old history [...] the brightly burning cross in the foreground...
        cross_emph = emphf(884, 736, -1046, -603)
        self.play(transformf(cross_emph), wuf(212.4))

        # ...behind which brutalized and deceased bodies accumulate into a towering pile of devastation.
        self.play(transformf(emphf(1913, 1330, -830, -89.5)), wuf(222.5))

        # With regards to the cross [...] "ghastly and shameful" emblem, going on to say:
        self.play(transformf(cross_emph), wuf(235.2))

        # \"This is the very way that they lynch the so-called negroes [...] you will be next."
        with register_font(Paths.common / "CMUSerif.ttf"):
            text = Text(
                text="“This is the very way that they lynch\n"
                "the so-called negroes, mutilating\n"
                "their bodies, and then offering you\n"
                "a piece of the rope that the man was\n"
                "hung with as a warning to you that\n"
                "you will be next.”",
                font_size=36,
                font="CMU Serif",
                slant=ITALIC,
            ).move_to((1.75, cross_emph.frame.get_y(), 0))

        self.play(emph.fill.animate.set_fill(opacity=1.0), wuf(236.2))
        self.play(Create(text), wuf(249.5))

        # In sum, Eugene Majied's 1963 graphic [...] constructive rather than destructive.
        self.play(Uncreate(text, run_time=0.5), Uncreate(emph), wuf(271.1))
        self.play(FadeOut(unite), wuf(273.1))


if __name__ == "__main__":
    UniteAndDoForSelf.run()
