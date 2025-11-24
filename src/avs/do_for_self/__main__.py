from typing import final, override

from manim import FadeIn, FadeOut, Group

from lib import MetaScene, Paths, Pixels, Wuf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class DoForSelf(MetaScene):
    voiceover = asset("voiceover.wav")

    @override
    def scene(self, wuf: Wuf) -> None:
        # Elijah Muhammad was a genius [...] was his ability...
        philly = image("philly.png")
        self.play(FadeIn(philly), wuf(17.6))

        # ...to create slogans and headlines. [...] he created headlines for the ads, too.
        god = image("god.png")
        self.play(FadeOut(philly), FadeIn(god), wuf(35.5))

        # So, he was trying to build [...] Elijah Muhammad approached that concept, and developed it.
        ladder = image("ladder.png")
        self.play(FadeOut(god), FadeIn(ladder), wuf(92.5))

        # His other major slogans [...] barred from achieving them by the Constitution itself.
        saviors = image("saviors.png")
        self.play(FadeOut(ladder), FadeIn(saviors), wuf(152.0))

        # So how does the overcome this hurdle? [...] effectively organize right out of the prisons.
        organizations = Group(
            image("hospital.png").scale(0.8).move_to((-3.1, 0, 0)),
            image("mosque.png").scale(0.8).move_to((3.1, 0, 0)),
        )

        self.play(FadeOut(saviors), FadeIn(organizations), wuf(176.8))

        # So, he essentially is saying [...] destructive habits and beliefs which they were habituated were his target.
        physician = image("physician.png")
        self.play(FadeOut(organizations), FadeIn(physician), wuf(203.2))

        # Other recovery organizations did the same thing [...] major elements of his program.
        keys = image("keys.png")
        self.play(FadeOut(physician), FadeIn(keys), wuf(251.6))

        # I think Elijah Muhammad just had an insight [...] And that, in essence, is "do-for-self".
        self.play(FadeOut(keys), FadeIn(ladder), wuf(279.0))
        self.play(FadeOut(ladder), wuf(281.0))


if __name__ == "__main__":
    DoForSelf.run()
