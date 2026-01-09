from dataclasses import dataclass
from Options import DefaultOnToggle, PerGameCommonOptions, Toggle, Range, Choice, OptionSet, DeathLink

@dataclass
class HotLavaOptions(PerGameCommonOptions):
    death_link: DeathLink