# Style

## Assets

For audio,
* commit tracks as `*.wav`,
* perform noise reduction if possible, then normalize to -3 dB,
* remove leading/ending silences (after taking a noise print),
* and ensure music has two seconds of linear fade in/out.

For video,
* commit the requisite image files as `*.png`,
* fit images to a 4K frame.
* and finalize videos with `/scripts/shrink` and `/scripts/border`.

Otherwise,
* commit fonts as `*.ttf`.

## Code

A new audiovisual presentation should be placed in `/src/avs/`, with a
`__main__.py` entry point, and an `assets/` folder. The entry point should be
of the below form.

```py
from typing import final, override
from lib import MetaScene, Paths, Pixels, Wuf

asset = Paths.assetf(__file__)
image = Pixels.imagef(asset)

@final
class Audiovisual(MetaScene):
    voiceover = asset("voiceover.wav")
    config = {"pixel_height": 1080, "pixel_width": 1920, "frame_rate": 60}

    @override
    def scene(self, wuf: Wuf) -> None:
        ...

if __name__ == "__main__":
    Audiovisual.run()
```

See prior presentations for examples of use of `/src/lib/` to load images,
draw `Emphasis` onto images, zoom into an image, etc. See the documentation for
`MetaScene` to play voiceover audio.

For slideshow-style presentations which only animate transitions between slides,
the `scene` function may instead be of the below form.

```py
@override
def scene(self, wuf: Wuf) -> None:
    ts = [25.2, 30.1, 32.1, 35.1, 44.2]
    slidesf(self, wuf, asset("slides/{}.png"), ts)
```

Then, slides `./assets/slides/*.png` will be loaded, and transitions will be
played automatically.
