from functools import partial
from typing import final, override

from manim import Create, FadeIn, FadeOut, Group, Restore, Transform

from lib import MetaScene, Paths, Pixels, Wuf, emphf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class BilialianNews(MetaScene):
    voiceover = asset("voiceover.wav")
    config = {"pixel_height": 1080, "pixel_width": 1920, "frame_rate": 60}

    @override
    def scene(self, wuf: Wuf) -> None:
        imagef = lambda x: image(x).scale(0.85)
        frame = self.camera.frame
        frame.save_state()

        # After Elijah Muhammad died in 1975, his son...
        he_lives_on = imagef("he-lives-on.png").move_to((-3, 0, 0))
        self.play(FadeIn(he_lives_on), wuf(5.0))

        # Warith al-Deen Mohammed [...] the traditional Islamic prayer in the mosque.
        wd_muhammad = imagef("wd-muhammad.png").move_to((3, 0, 0))
        self.play(FadeIn(wd_muhammad), wuf(34.3))

        # Another change was in the name of the newspaper [...] signaling the Nation's new directions.
        imagef = lambda x: image(x).scale(0.75)
        nameswitch = Group(
            imagef("header.png").move_to((-1.15, 1.5, 0)),
            imagef("superimposed.png").move_to((-1.15, -1.5, 0)),
            imagef("beginning.png").move_to((5.7, 0, 0)),
        )
        self.play(FadeOut(he_lives_on), FadeOut(wd_muhammad), wuf(35.9))
        self.play(FadeIn(nameswitch, lag_ratio=0.5), wuf(93.7))

        # The front page of [...] includes the headline...
        master_bilal = image("master-bilal.png")
        self.play(FadeOut(nameswitch), FadeIn(master_bilal), wuf(102.4))

        # "Master Bilal," written in large block letters.
        emph = emphf(236, 1482, 1, 561)
        self.play(Create(emph), wuf(107.9))

        # Below the headline is [...] the Muslim sunrise in the West.
        transformf = partial(Transform, emph)
        self.play(transformf(emphf(936, 824, 296, -124)), wuf(150.1))

        # In the word bubble above the muezzin's head, [...] "Come to Growth by Cultivation."
        self.play(transformf(emphf(162, 824, 296, 263)), wuf(173.5))

        # The NOI artist Eugene Majied also signed his name in Arabic, rather than the Latin letters he previously used.
        emph_majied = emphf(28, 53, 630.5, -563)
        self.play(
            frame.animate.move_to((emph_majied.frame_x, emph_majied.frame_y, 0)).set(width=emph_majied.frame_width * 4),
            transformf(emph_majied),
            wuf(184.6),
        )

        # Around the sun's aureola appear the words, [...] as something sweet.
        emph_honey = emphf(261, 320, 296, 21.5)
        self.play(
            frame.animate.move_to((emph_honey.frame_x, emph_honey.frame_y, 0)).set(width=emph_honey.frame_width * 4),
            transformf(emph_honey),
            wuf(216.9),
        )

        # This diversity is reflected [...] listening to the call...
        emph_crowd = emphf(514, 810, 299, -334)
        self.play(
            frame.animate.move_to((emph_crowd.frame_x, emph_crowd.frame_y, 0)).set(width=emph_crowd.frame_width * 2),
            transformf(emph_crowd),
            wuf(223.8),
        )

        # ...as well as in the photographs... [...] with the caption...
        muslims_come_together = image("muslims-come-together.png")
        self.play(Restore(frame), FadeOut(master_bilal), FadeOut(emph), FadeIn(muslims_come_together), wuf(243.7))

        # "Muslims of all nationalities and colors kneel en masse in prayer."
        emph = emphf(355, 889, 348, -277.5)
        self.play(
            frame.animate.move_to((emph.frame_x, emph.frame_y, 0)).set(width=emph.frame_width * 2),
            Create(emph),
            wuf(251.7),
        )

        # Two weeks later, the November 7, 1975 issue [...] created and edited by the poet Sonia Sanchez.
        new_frontiers = image("new-frontiers.png")
        self.play(Restore(frame), FadeOut(muslims_come_together), FadeOut(emph), FadeIn(new_frontiers), wuf(271.5))

        # The illustration shows Bilal, [...] about Bilal and the call to prayer.
        emph = emphf(619, 903, -333, 764.5)
        self.play(
            frame.animate.move_to((emph.frame_x, emph.frame_y, 0)).set(width=emph.frame_width * 2),
            Create(emph),
            wuf(291.8),
        )

        # Entitled, "Did you know?," [...] biographical details about Bilal from the Islamic tradition.
        emph_title = emphf(608, 637, 469, 728)
        transformf = partial(Transform, emph)
        self.play(
            frame.animate.move_to((emph_title.frame_x, emph_title.frame_y, 0)).set(width=emph_title.frame_width * 2),
            transformf(emph_title),
            wuf(315.0),
        )

        # She also transcribes the words [...] in both transliterated Arabic and in English translation.
        prayer_call = imagef("prayer-call.png").move_to((3.75, 0, 0))
        self.play(
            Restore(frame),
            FadeOut(emph),
            new_frontiers.animate.move_to((-2.25, 0, 0)),
            FadeIn(prayer_call),
            wuf(327.7),
        )

        # [Pause between "...translation." and "The bismillah..."]
        second_resurrection = image("second-resurrection.png")
        self.play(FadeOut(new_frontiers), FadeOut(prayer_call), FadeIn(second_resurrection), wuf(329.6))

        # The bismallah, "In the name of God," [...] just after the death of Elijah Muhammad.
        emph = emphf(67, 343, -11.5, 383.5)
        self.play(
            frame.animate.move_to((emph.frame_x, emph.frame_y, 0)).set(width=emph.frame_width * 4),
            Create(emph),
            wuf(341.9),
        )

        # It was the culmination of three issues of Muhammad Speaks [...] as he turned the NOI toward Sunni Islam.
        self.play(Restore(frame), FadeOut(emph), wuf(367.5))

        # The first issue of Bilalian News [...] It also reinterpreted...
        lost_found_nation = image("lost-found-nation.png")
        self.play(FadeOut(second_resurrection), FadeIn(lost_found_nation), wuf(380.4))

        # ...Eugene Majied's classic image [...] the sun rising behind their clasped hands. In the...
        handshake = image("handshake.png")
        self.play(FadeOut(lost_found_nation), FadeIn(handshake), wuf(396.0))

        # ...new illustration for Bilalian News, [...] its first muezzin calling Muslims to prayer.
        self.play(FadeOut(handshake), FadeIn(lost_found_nation), wuf(435.3))
        self.play(FadeOut(lost_found_nation), wuf(437.3))


if __name__ == "__main__":
    BilialianNews.run()
