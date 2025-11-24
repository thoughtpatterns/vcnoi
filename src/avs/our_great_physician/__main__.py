from functools import partial
from typing import final, override

from manim import Create, FadeIn, FadeOut, Transform, Uncreate

from lib import MetaScene, Paths, Pixels, Wuf, emphf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class OurGreatPhysician(MetaScene):
    voiceover = asset("voiceover.wav")

    @override
    def scene(self, wuf: Wuf) -> None:
        # Many early scholars of the Nation of Islam [...] was seen as a cult leader.
        coliseum = image("coliseum.png")
        self.play(FadeIn(coliseum), wuf(29.5))

        # But that is not how tens of thousands of his followers [...] had saved their lives.
        blackman = image("blackman.png")
        self.play(FadeOut(coliseum), FadeIn(blackman), wuf(49.5))

        # Elijah Muhammad's interpretation of Islam offered [...] Eugene Majied's cartoon titled...
        physician = image("physician.png")
        self.play(FadeOut(blackman), FadeIn(physician), wuf(58.5))

        # ..."Our Great Physician" illustrates.
        emph = emphf(55, 755, -365, 1051)
        self.play(Create(emph), wuf(61.8))

        # Signing his name "Majied XXX" on the bed, the NOI cartoonist takes...
        transformf = partial(Transform, emph)
        self.play(transformf(emphf(45, 180, -522, -559.5)), wuf(67.9))

        # ...a verse from the Qur'an that most Muslims [...] Instead, Majied applies it to...
        self.play(transformf(emphf(310, 1385, 2.5, -913)), wuf(79.0))

        # Elijah Muhammad, an African American man born in 1897 in Sandersville [...] created by white supremacy.
        self.play(transformf(emphf(1561, 706, 353, 71.5)), wuf(119.1))

        # The patient's medical diagnosis [...] Black and Muslim people.
        self.play(transformf(emphf(373, 368, -542, -252.5)), wuf(137.3))

        # The patient reaches toward the one man who can cure him from the wounds of physical and mental slavery...
        self.play(transformf(emphf(1305, 678, -191, -138.5)), wuf(144.5))

        # ...represented in this cartoon by a sneering white man [...] manifestations of an enslaved mentality.
        self.play(transformf(emphf(1110, 546, -459, 287)), wuf(160.7))

        # The symbols of that old are scattered beneath his hospital bed. They include...
        self.play(transformf(emphf(434, 990, -235, -581)), wuf(165.9))

        # Christianity, represented by a cross pendant;
        self.play(transformf(emphf(165, 176, 79, -713.5)), wuf(169.7))

        # violent street crime, represented by the handgun;
        self.play(transformf(emphf(71, 149, 156.5, -630.5)), wuf(173.2))

        # and sexual immorality, represented by the pornographic magazine entitled "Lust."
        self.play(transformf(emphf(193, 343, -493.5, -656.5)), wuf(180.6))

        # For members of the Nation of Islam [...] as they walked through life.
        self.play(Uncreate(emph), wuf(204.6))
        self.play(FadeOut(physician), wuf(206.6))


if __name__ == "__main__":
    OurGreatPhysician.run()
