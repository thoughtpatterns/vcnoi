from typing import final, override

from lib import MetaScene, Paths, Wuf, slidesf

asset = Paths.assetf(__file__)


@final
class RashidAlDin(MetaScene):
    voiceover = asset("voiceover.wav")

    @override
    def scene(self, wuf: Wuf) -> None:
        ts = [
            43.0,  # Hello. My name is Stefan Kamola [...] during the Mongol period.
            86.0,  # Chinggis Khan, the founder of the Mongol Empire [...] ruled Iran as Muslim sovereigns.
            128.0,  # One of the most influential individuals [...] future rulers and administrators.
            164.7,  # In this talk, I will describe Rashid al-Din's life [...] realities of Mongol rule.
            205.4,  # Chinggis Khan's invasion of 1219 [...] followers of the Isma'ili Shi'i Imam.
            242.4,  # These leaders -—- caliph and imam [...] into a royal dynastic state.
            267.5,  # Hülegü secured the surrender of the Isma'ili imam [...] the hot lowlands around Baghdad.
            291.8,  # Between waves of Mongol invasion [...] Hülegü's son moved the capital there.
            324.8,  # From the age of ten to fifty [...] to which we will turn shortly.
            355.3,  # Each time he presented one of these works to Öljeitü [...] the outskirts of Tabriz, shown here.
            401.7,  # Rashid al-Din's works illuminate the Mongol world [...] advertise the credentials of his family.
            447.1,  # Rashid al-Din was granted unprecedented access [...] the branch that ruled Iran.
            516.1,  # Two major themes carry through this story: [...] the former Seljuq sultans of the region.
            566.0,  # One thing Ghazan's Mamluk rivals did have was a strong tradition [...] figures of the Buddha.
            609.8,  # The Blessed History is our best single source [...] different parts of this portion of the work.
            657.1,  # The second part contains summary histories [...] produced by the subject societies themselves.
            725.1,  # The same is notable in the case [...] Rashid al-Din held it in his own hands seven centuries ago.
            803.5,  # Beyond this historical masterpiece [...] beyond the Buddhist monk's understanding.
            833.1,  # Other questions were presented [...] the Prophet's human-headed, flying steed.
            889.8,  # Rashid al-Din also engaged [...] Greek-derived philosophy and logic.
            971.3,  # A polymath, Rashid al-Din was also inspired [...] to learn numerous languages.
            1043.0,  # Despite his illustrious career in government [...] experts from Europe to China.
            1053.0,  # [References.]
            1055.0,  # [Fade out.]
        ]

        slidesf(self, wuf, asset("slides/{}.png"), ts)


if __name__ == "__main__":
    RashidAlDin.run()
