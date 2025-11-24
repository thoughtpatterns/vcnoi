from functools import partial
from typing import final, override

from manim import Create, FadeIn, FadeOut, Restore, Transform, Uncreate

from lib import MetaScene, Paths, Pixels, Wuf, emphf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class WorldSerpent(MetaScene):
    voiceover = asset("voiceover.wav")
    config = {"pixel_height": 720, "pixel_width": 1280, "frame_rate": 60}

    @override
    def scene(self, wuf: Wuf) -> None:
        frame = self.camera.frame

        # From 1964, the fourth year of its publication [...] iconic illustrations by...
        handshake = image("handshake.png")
        self.play(FadeIn(handshake), wuf(14.9))

        # ...the artist and illustrator Eugene Majied.
        frame.save_state()
        emph = emphf(47, 236, 178, 339.5)

        self.play(
            frame.animate.move_to((emph.frame_x, emph.frame_y, 0)).set(width=emph.frame_width * 4),
            Create(emph),
            wuf(18.7),
        )

        # The top of each cover page showed the torsos of two Black men [...] so as to clasp hands.
        transformf = partial(Transform, emph)
        self.play(Restore(frame), transformf(emphf(400, 1612, -37, 494)), wuf(34.3))

        # But it's another image that I want to focus on, now. [...] Majied titled this illustration...
        serpent = image("serpent.png")
        self.play(FadeOut(emph), FadeOut(handshake), FadeIn(serpent), wuf(63.9))

        # "The Serpent Deceived the Whole World," and he included, as a sort of caption...
        emph = emphf(254, 664, -1150, 902)
        self.play(Create(emph), wuf(71.1))

        # ...part of a verse from the King James version [...] his angels were cast out with him.
        transformf = partial(Transform, emph)
        self.play(transformf(emphf(76, 409, -1216.5, 813)), wuf(102.6))

        # In Majied's drawing, that "old serpent" bears...
        self.play(Uncreate(emph), wuf(106.6))

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
        self.play(Restore(frame), transformf(emphf(401, 969, 1007.5, -827.5)), wuf(202.1))

        # Which "Muhammad" is referred to [...] ought to include this powerful composition.
        self.play(Uncreate(emph), wuf(387.7))
        self.play(FadeOut(serpent), wuf(389.7))


if __name__ == "__main__":
    WorldSerpent.run()
