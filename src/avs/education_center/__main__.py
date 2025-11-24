from typing import final, override

from manim import BLACK, Create, FadeIn, FadeOut, Group, Rectangle, Restore, Uncreate, config

from lib import MetaScene, Paths, Pixels, Wuf, emphf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)


@final
class EducationCenter(MetaScene):
    voiceover = asset("voiceover.wav")

    @override
    def scene(self, wuf: Wuf) -> None:
        imagef = lambda x: image(x).scale(0.45)
        frame = self.camera.frame

        # Anyone who looked through an issue [...] with children learning about...
        educators = Group(
            imagef("sheard.png").move_to((-2.7, 1.9, 0)),
            imagef("iqra.png").move_to((-2.7, -1.9, 0)),
            imagef("headstart.png").move_to((2.7, 1.9, 0)),
            imagef("misprint.png").move_to((2.7, -1.9, 0)),
        )

        self.play(FadeIn(educators, lag_ratio=2, run_time=11), wuf(26.3))

        # ...the great accomplishments of Black and African peoples.
        omar = Group(
            Rectangle(
                color=(0, 0, 0, 0),
                height=config.frame_height,
                width=config.frame_width,
                fill_color=BLACK,
                fill_opacity=0.5,
            ),
            imagef("omar.png"),
        )

        self.play(FadeIn(omar), wuf(31.5))

        # A lot of the artwork was focused on independent primary schools. But in the mid-1960s...
        center = image("center.png")
        self.play(FadeOut(omar), FadeOut(educators), FadeIn(center), wuf(36.6))

        # Eugene Majied started to illustrate a series that was focused on Black-run colleges and universities.
        frame.save_state()
        emph = emphf(55, 94, 1342.5, -90.5)

        self.play(
            frame.animate.move_to((emph.frame_x, emph.frame_y, 0)).set(width=emph.frame_width * 16),
            Create(emph),
            wuf(45.7),
        )

        # Now, the drawings were actually part of a fundraising campaign [...] learn to rise up and do for self.
        self.play(Restore(frame), Uncreate(emph), wuf(58.6))

        # Majied's illustrations included these imposing drawings [...] like a December 1965 issue that read...
        prepare = image("prepare.png")
        self.play(FadeOut(center), FadeIn(prepare), wuf(96.6))

        # ..."Re-educate the Black man so he can qualify for his own life."
        emph = emphf(119, 1091, 125.5, 656.5)
        self.play(Create(emph), wuf(103.0))

        # The effort to establish an independent Black university [...] capacity for independent Black life.
        self.play(FadeOut(emph), FadeOut(prepare), FadeIn(center), wuf(134.0))

        # Majied's drawings signaled to readers [...] the Nation of Islam and all Black people.
        program = image("program.png")
        self.play(FadeOut(center), FadeIn(program), wuf(156.4))

        # Majied's imagery in the education campaign [...] professionals would not only exist, they would thrive.
        self.play(FadeOut(program), FadeIn(educators), wuf(185.8))
        self.play(FadeOut(educators), wuf(187.8))


if __name__ == "__main__":
    EducationCenter.run()
