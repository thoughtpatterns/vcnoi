from functools import partial
from typing import final, override

from manim import (
    DOWN,
    ITALIC,
    ORIGIN,
    Create,
    FadeIn,
    FadeOut,
    Group,
    Text,
    Transform,
    Uncreate,
    config,
    register_font,
)

from lib import MetaScene, Paths, Pixels, Wuf, emphf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class ButNeverAWordAboutSelfDefense(MetaScene):
    voiceover = asset("voiceover.wav")
    # config = {"pixel_height": 1080, "pixel_width": 1920, "frame_rate": 60}

    @override
    def scene(self, wuf: Wuf) -> None:
        # In the summer of 1963 [...]
        never_a_word = image("never-a-word.png")
        self.play(FadeIn(never_a_word), wuf(36.8))

        # On a national stage Malcolm X [...]
        with register_font(Paths.common / "CMUSerif.ttf"):
            caption = Text(
                "Lloyd Yearwood, Malcolm X speaking at a podium, Harlem, early 1960s\n"
                "Smithsonian National Museum of African American History and Culture, 2014.150.5.1\n"
                "© Estate of Lloyd W. Yearwood",
                font_size=28,
                font="CMU Serif",
                slant=ITALIC,
            )
        malcolm_x_image = image("malcolm-x.png")
        caption.scale(min(1, malcolm_x_image.width / caption.width))
        gap = Pixels.to_units(54)
        malcolm_x_image.scale_to_fit_height(config.frame_height - caption.height - gap)
        caption.scale(min(1, malcolm_x_image.width / caption.width))
        malcolm_x = Group(caption, malcolm_x_image).arrange(DOWN, buff=gap).move_to(ORIGIN)
        self.play(FadeOut(never_a_word), FadeIn(malcolm_x), wuf(50.6))

        # Muhammad Speaks regularly published commentary [...]
        self.play(FadeOut(malcolm_x), FadeIn(never_a_word), wuf(57.2))

        # But it was Eugene Majied's political cartoons [...]
        emph = emphf(83.84, 362.55, 722.09, -1024.21)
        self.play(Create(emph), wuf(75.5))

        # This illustration by Eugene Majied is titled...
        self.play(Uncreate(emph), wuf(79.0))

        # ..."But Never A Word About Self-Defense!"
        emph = emphf(206.89, 3500.67, -36.2, 879.44)
        self.play(Create(emph), wuf(82.0))

        # Here, a Black woman lays on her back [...]
        transformf = partial(Transform, emph)
        self.play(transformf(emphf(444, 1207, -127, -843)), wuf(88.8))

        # ...as two white police officers [...]
        self.play(transformf(emphf(1560.44, 1391.1, -216.27, -288.92)), wuf(105.8))

        # ...towards "Rev. M. L. King," shown crouching on his hands [...]
        self.play(transformf(emphf(971.13, 706.41, 611.7, -496.72)), wuf(118.8))

        # ...saying "If there is any blood spilled in the streets, let it be our blood!"
        self.play(transformf(emphf(1770.34, 1029.75, 450.03, -97.11)), wuf(123.7))

        # Behind them, other officers [...]
        self.play(Uncreate(emph), wuf(126.9))

        # ...with one officer dangling a woman by her ankles...
        emph = emphf(1172.59, 435.55, -679.56, -90.18)
        self.play(Create(emph), wuf(129.7))

        # ...as other white men violently tear the clothing [...]
        transformf = partial(Transform, emph)
        self.play(transformf(emphf(927.7, 970.03, 475.06, 7.54)), wuf(139.3))

        # In the furthest background, a courthouse bears [...]
        self.play(transformf(emphf(690.04, 499.49, -695.25, 447.26)), wuf(147.5))

        # Majied's image aims to undermine the moral high ground of nonviolence [...]
        self.play(Uncreate(emph), wuf(254.3))

        # ...one of his popular drawings depicts "Uncle Sam" as a "Dr. Jekyll and Mr. Hyde," [...]
        jekyll_and_hyde = image("jekyll-and-hyde.png")
        self.play(FadeOut(never_a_word), FadeIn(jekyll_and_hyde), wuf(265.3))

        # ...In many Islamic communities, including the Nation of Islam, [...]
        self.play(FadeOut(jekyll_and_hyde), FadeIn(never_a_word), wuf(289.7))
        self.play(FadeOut(never_a_word), wuf(291.7))


if __name__ == "__main__":
    ButNeverAWordAboutSelfDefense.run()
