from functools import partial
from pathlib import Path
from types import SimpleNamespace
from typing import Final, final


@final
class Paths(SimpleNamespace):  # noqa: D101
    root: Final = Path(__file__).parent.parent.parent
    common: Final = root / "common"
    media: Final = root / "media"

    @staticmethod
    def assetp(__file__: str, filename: str, directory: str = "assets") -> Path:
        """Get the absolute path of an asset in the current module directory.

        As an example, if `asset("voiceover.wav")` were called in `do_for_self`, we would return
        `"/path/to/vcnoi/src/avs/do_for_self/assets/voiceover.wav"`.
        """
        return Path(__file__).parent / directory / filename

    @staticmethod
    def asset(__file__: str, filename: str, directory: str = "assets") -> str:
        """Wrap `assetp` with `str()`."""
        return str(Paths.assetp(__file__, filename, directory))

    @staticmethod
    def assetpf(__file__: str) -> partial[Path]:
        """Simplify partial `assetp` application."""
        return partial(Paths.assetp, __file__)

    @staticmethod
    def assetf(__file__: str) -> partial[str]:
        """Simplify partial `assetp` application."""
        return partial(Paths.asset, __file__)


__all__ = ["Paths"]
