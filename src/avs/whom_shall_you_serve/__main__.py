from functools import partial
from typing import final, override

from manim import Create, FadeIn, FadeOut, Transform, Uncreate

from lib import MetaScene, Paths, Pixels, Wuf, emphf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class WhomShallYouServe(MetaScene):
    voiceover = asset("voiceover.wav")

    @override
    def scene(self, wuf: Wuf) -> None:
        # Elijah Muhammad warned against Black integration [...] including this cartoon entitled...
        whom = image("whom.png")
        self.play(FadeIn(whom), wuf(19.9))

        # ..."Whom Shall You Serve?" In this graphic made by NOI artist...
        emph = emphf(121, 1329, -0.5, 1002.5)
        self.play(Create(emph), wuf(24.6))

        # ...Eugene Majied...
        transformf = partial(Transform, emph)
        self.play(transformf(emphf(112, 192, 95, -991), run_time=0.5), wuf(26.1))

        # ...and published in Muhammad Speaks in September 1964 [...] in rather Manichaean terms.
        self.play(Uncreate(emph), wuf(38.3))

        # On the left, Majied rhetorically asks his viewers...
        left_emph = emphf(2005, 1455, -714.5, -67)
        transformf = partial(Transform, emph := left_emph.copy())
        self.play(Create(emph), wuf(42.2))

        # ...whether they shall serve Satan by illustrating...
        self.play(transformf(emphf(179, 781, -1020.5, 21.5)), wuf(45.2))

        # ...a decrepit church over whose entrance is inscribed...
        self.play(transformf(emphf(889, 679, -333.5, -113.5)), wuf(48.4))

        # ..."White Man's Slavery."
        self.play(transformf(emphf(188, 297, -269.5, -261)), wuf(51.0))

        # A hunched-over Black man follows in the tracks of...
        self.play(transformf(emphf(705, 227, -1326.5, -691.5)), wuf(54.1))

        # ...affluent Christians decked in fur coats and top hats...
        self.play(transformf(emphf(822, 836, -825, -622)), wuf(58.2))

        # ...while a smoldering sky...
        self.play(transformf(emphf(816, 1457, -721.5, 525)), wuf(60.0))

        # ...engulfs the necrotic body of Christ nailed to a flaming cross [...] throughout the NOI's visual culture.
        self.play(transformf(emphf(949, 528, -282, 446.5)), wuf(71.3))

        # With a bridging ellipsis to the right frame, [...] whether his viewers are willing to serve God. Here...
        self.play(transformf(emphf(180, 1140, 765, 19)), wuf(81.3))

        # ...a domed mosque whose entrance is emblazoned with...
        mosque_emph = emphf(1193, 789, 393.5, 43.5)
        self.play(transformf(mosque_emph), wuf(84.0))

        # ...the Flag of Islam and the inscription...
        self.play(transformf(emphf(105, 111, 494.5, -155.5)), wuf(85.9))

        # ..."God's Freedom" welcomes...
        self.play(transformf(emphf(72, 464, 462, -225)), wuf(87.5))

        # ...a row of Muslim faithful --- including...
        self.play(transformf(emphf(771, 921, 929.5, -644.5)), wuf(90.5))

        # ...NOI women clad in their distinctive white robes and hijabs --- who make their way into...
        self.play(transformf(emphf(771, 695, 1042.5, -644.5)), wuf(95.9))

        # ...an architectural stand-in for deliverance from white supremacy and Christian oppression.
        self.play(transformf(mosque_emph), wuf(101.8))

        # Rays of light pierce through the clouds, illuminating the scene.
        self.play(transformf(emphf(769, 1439, 729.5, 547.5)), wuf(106.4))

        # For the NOI, this type of either-or proposition [...] these types of images execrate...
        self.play(Uncreate(emph), wuf(121.7))

        # Christian disbelief, while concurrently...
        transformf = partial(Transform, emph := left_emph)
        self.play(Create(emph), wuf(124.0))

        # ...praising and proclaiming a loyalty to Islam.
        right_emph = emphf(2005, 1459, 719.5, -67)
        self.play(transformf(right_emph), wuf(128.2))

        # Not limited to Islamic religious spheres alone [...] across multiple registers, including religious ones.
        self.play(Uncreate(emph), wuf(170.0))
        self.play(FadeOut(whom), wuf(172.0))


if __name__ == "__main__":
    WhomShallYouServe.run()
