from functools import partial
from typing import final, override

from manim import ITALIC, Create, FadeIn, FadeOut, Restore, Text, Transform, Uncreate, register_font

from lib import MetaScene, Paths, Pixels, Wuf, emphf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class WorldSerpent(MetaScene):
    voiceover = asset("voiceover.wav")
    # config = {"pixel_height": 720, "pixel_width": 1280, "frame_rate": 15}

    @override
    def scene(self, wuf: Wuf) -> None:  # noqa: PLR0915
        frame = self.camera.frame

        # From 1964, the fourth year of its publication [...] iconic illustrations by...
        handshake = image("handshake.png")
        self.play(FadeIn(handshake), wuf(14.9))

        # ...the artist and illustrator Eugene Majied.
        frame.save_state()
        emph = emphf(36, 213, 173.5, 305)

        self.play(
            frame.animate.move_to((emph.frame_x, emph.frame_y, 0)).set(width=emph.frame_width * 4),
            Create(emph),
            wuf(18.7),
        )

        # The top of each cover page showed the torsos of two Black men [...] so as to clasp hands.
        transformf = partial(Transform, emph)
        emph_hands = emphf(374, 1476, -28, 438)
        self.play(
            transformf(emph_hands),
            frame.animate.move_to((emph_hands.frame_x, emph_hands.frame_y, 0)).set(width=emph_hands.frame_width * 1.2),
            wuf(34.3),
        )

        # But it's another image that I want to focus on, now. [...] Majied titled this illustration...
        serpent = image("serpent.png")
        self.play(Restore(frame), FadeOut(emph), FadeOut(handshake), FadeIn(serpent), wuf(63.9))

        # "The Serpent Deceived the Whole World," and he included, as a sort of caption...
        emph = emphf(254, 664, -1150, 902)
        self.play(Create(emph), wuf(71.1))

        # ...part of a verse from the King James version [...] chapter 12, verse 9.
        transformf = partial(Transform, emph)
        self.play(transformf(emphf(76, 409, -1216.5, 813)), wuf(80.5))

        # The caption reads...
        scale = 0.6
        self.play(FadeOut(emph, run_time=0.5), serpent.animate.set_y(1.35).scale(scale), wuf(82.9))

        # \"And the great dragon was cast out [...] and his angels were cast out with him."
        with register_font(Paths.common / "CMUSerif.ttf"):
            text = Text(
                text="“And the great dragon was cast\n"
                "out, that old serpent, called the\n"
                "Devil, and Satan, which deceiveth\n"
                "the whole world: he was cast out\n"
                "into the earth, and his angels\n"
                "were cast out with him.”",
                font_size=32,
                font="CMU Serif",
                slant=ITALIC,
            ).set_y(-2.55)

        self.play(Create(text), wuf(100.5))

        # In Majied's drawing, that "old serpent" bears...
        self.play(Uncreate(text), wuf(102.7))
        self.play(serpent.animate.set_y(0).scale(1 / scale), wuf(106.6))

        # ...the face of a fiendish Uncle Sam, [...] Uncle Sam's white-haired head rises out of...
        emph = emphf(566, 330, 156, 484)
        self.play(Create(emph), wuf(123.5))

        # ...the United States.
        transformf = partial(Transform, emph)
        self.play(transformf(emphf(555, 881, 80.5, 162.5)), wuf(126.4))

        # His gaping mouth contains recent human victims, identified as "Indians" and "Negroes."
        frame.save_state()
        self.play(
            frame.animate.move_to((emph.frame_x, emph.frame_y, 0)).set(width=emph.frame_width * 4),
            transformf(emphf(228, 367, 154.5, 349)),
            wuf(135.4),
        )

        # And just under Uncle Sam's teeth, as part of the serpent's fangs [...] "Negro Preachers and Politicians."
        self.play(transformf(emphf(103, 120, 134, 405.5)), wuf(147.1))

        # As you scan the details in the rest of the illustration [...] But there is one exception to humanity's fate.
        self.play(Restore(frame), Uncreate(emph), wuf(168.5))

        # Only in Arabia, identified as the "Garden of Paradise," [...] out of their homeland and toward the serpent.
        frame.save_state()
        emph = emphf(431, 360, 1337, 234.5)

        self.play(
            frame.animate.move_to((emph.frame_x, emph.frame_y, 0)).set(width=emph.frame_width * 4),
            Create(emph),
            wuf(189.8),
        )

        # A caption nearby declares, that: "To heal the poisonous bite [...] the medicine that God gives Muhammad."
        transformf = partial(Transform, emph)
        emph_heal = emphf(401, 969, 1007.5, -827.5)
        self.play(
            transformf(emph_heal),
            frame.animate.move_to((emph_heal.frame_x, emph_heal.frame_y, 0)).set(width=emph_heal.frame_width * 2),
            wuf(202.1),
        )

        # Which "Muhammad" is referred to [...] and not "gave".
        self.play(Restore(frame), FadeOut(emph, run_time=0.5), wuf(216.5))

        # I have no doubt that Majied is referring here to Elijah Muhammad [...] Muhammad as its messenger.
        apostle = image("apostle.png")
        self.play(FadeOut(serpent), FadeIn(apostle), wuf(264.7))

        # Moreover, I find it illustrative [...] conscious or unconscious censorship.
        scale = 0.625
        serpent = serpent.set_x(-2.875).set_y(0.75).scale(scale)
        ouroboros = image("ouroboros.png").set_z_index(-1).set_x(4).set_y(0.75).scale(scale)
        self.play(FadeOut(apostle), FadeIn(serpent), FadeIn(ouroboros), wuf(265.2))

        with register_font(Paths.common / "CMUSerif.ttf"):
            text = Text(
                text="“An ouroboros in a 1478 drawing\nin an alchemical tract,” Wikimedia Commons.",
                font_size=36,
                font="CMU Serif",
                slant=ITALIC,
            ).set_y(-2.875)

        self.play(Create(text), wuf(326.8))

        # To me, the outstanding distinction [...] ought to include this powerful composition.
        self.play(Uncreate(text), wuf(327.3))
        self.play(serpent.animate.set_x(0).set_y(0).scale(1 / scale), ouroboros.animate.set_x(0).set_y(0), wuf(327.8))
        self.remove(ouroboros)
        self.play(wuf(387.7))
        self.play(FadeOut(serpent), wuf(389.7))


if __name__ == "__main__":
    WorldSerpent.run()
