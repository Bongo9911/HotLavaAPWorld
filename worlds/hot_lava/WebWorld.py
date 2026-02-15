from BaseClasses import Tutorial
from ..AutoWorld import WebWorld


class HotLavaWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Hot Lava for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Bongo9911"]
    )]

    # option_groups = hot_lava_options_groups # TODO