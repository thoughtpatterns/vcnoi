from abc import ABC, abstractmethod
from typing import Any, ClassVar, override

from manim import MovingCameraScene
from manim import config as mconfig

from lib.intro import intro
from lib.paths import Paths
from lib.timestamp import Timestamp, Wuf, wuf


class MetaScene(MovingCameraScene, ABC):
    """Initialize voiceovers, timestamps, `render()` calls, etc., to reduce duplicate code among scenes."""

    voiceover: str | None = None
    intro: bool = True
    config: ClassVar[dict[str, Any]] = {}

    @override
    def construct(self) -> None:
        (introf := (lambda: intro(self)) if self.intro else lambda: None)()

        self.wait(1)

        if self.voiceover:
            self.add_sound(self.voiceover)

        t = Timestamp()
        self.scene(wuf(t))

        introf()

    @abstractmethod
    def scene(self, wuf: Wuf) -> None:
        """Add content to the scene (as with `Scene.construct`)."""
        ...

    @classmethod
    def run(cls) -> None:
        """Apply the class configuration, then render the class scene."""
        defaults = {
            "disable_caching": True,
            "media_dir": Paths.media,
            "preview": True,
            # Replicate `-ql`.
            "pixel_height": 480,
            "pixel_width": 854,
            "frame_rate": 15,
        }

        [setattr(mconfig, k, v) for k, v in (defaults | cls.config).items()]
        cls().render()


__all__ = ["MetaScene"]
