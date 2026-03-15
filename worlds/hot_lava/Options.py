from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING
from Options import DefaultOnToggle, PerGameCommonOptions, TextChoice, Toggle, Range, Choice, OptionSet, DeathLink
from .Data import game_world_dict

if TYPE_CHECKING:
    from .World import HotLavaWorld

class WorldUnlockLogic(Choice):
    """
    How additional worlds will be unlocked in-game
    """
    
    display_name = "World Unlock Logic"
    
    option_star_items = 0
    option_world_item = 1
    
    default = option_world_item
    
class ForceFieldLogic(Choice):
    """
    How force fields will be deactivated in-game
    """
    
    display_name = "Force Field Logic"
    
    option_vanilla = 0
    option_force_field_item = 1
    option_disabled = 2
    
    default = option_disabled
    
class EnabledWorlds(OptionSet):
    """
    The list of worlds that are enabled for checks in-game
    """
    
    display_name = "Enabled Worlds"
    
    valid_keys = {
        "gym_class",
        "playground",
        "school",
        "wholesale",
        "master_class",
        "basement",
        "roccos_arcade",
    }
    
    default = {
        "gym_class",
        "playground",
        "school",
        "wholesale",
        "master_class",
        "basement",
        "roccos_arcade",
    }
    
class WorldSelect(Choice):
    """
    Select a world from the list of worlds
    """
    
    option_random_world = 0
    option_gym_class = 1
    option_playground = 2
    option_school = 3
    option_wholesale = 4
    option_master_class = 5
    option_basement = 6
    option_roccos_arcade = 7
    
class StartWorld(WorldSelect):
    """
    The world that you will have unlocked at the start
    """
    
    display_name = "Start World"
    
    default = 1
    
class LastWorld(WorldSelect):
    """
    The last world you will unlock or the world you will be required to complete to complete your game
    """
    
    display_name = "Last World"
    
    default = 5
    
class EnableTimeStars(Toggle):
    """
    Whether stars for completing a course within a certain amount of time will be enabled as checks
    """
    display_name = "Enable Time Stars"

class EnableNoDeathsStars(Toggle):
    """
    Whether stars for completing a course without dying will be enabled as checks
    """
    display_name = "Enable No Deaths Stars"
    
class EnableCollectibleStars(Toggle):
    """
    Whether stars for picking up course collectibles (Golden Pins, G.A.T. Comics, etc.) will be enabled as checks
    """
    display_name = "Enable Collectible Stars"
    
class EnableChallengeStars(Toggle):
    """
    Whether stars for completing course-specific challenges (No Swinging, Reach a Target Speed, etc.) will be enabled as checks
    """
    display_name = "Enable Challenge Stars"
    
class EnablePogoStars(DefaultOnToggle):
    """
    Whether stars for completing Pogo trials will be enabled as checks
    """
    display_name = "Enable Pogo Stars"

class EnableTinyToyStars(DefaultOnToggle):
    """
    Whether stars for completing Tiny Toy trials will be enabled as checks
    """
    display_name = "Enable Tiny Toy Stars"

class EnableJetpackStars(DefaultOnToggle):
    """
    Whether stars for completing Jetpack trials will be enabled as checks
    """
    display_name = "Enable Jetpack Stars"
    
class EnableChaseTheGradeStars(DefaultOnToggle):
    """
    Whether stars for completing Chase the Grade trials will be enabled as checks
    """
    display_name = "Enable Chase the Grade Stars"

class EnableAllCourseStars(Toggle):
    """
    Whether stars for completing All Course Marathon will be enabled as checks
    """
    display_name = "Enable All Course Stars"

class EnableBuddyStars(Toggle):
    """
    Whether stars for completing courses (except chase courses) with Buddy will be enabled as checks
    """
    display_name = "Enable Buddy Stars"

class EnableBuddyChaseStars(DefaultOnToggle):
    """
    Whether stars for completing chase courses with Buddy will be enabled as checks
    """
    display_name = "Enable Buddy Stars"

@dataclass
class HotLavaOptions(PerGameCommonOptions):
    # world_unlock_logic: WorldUnlockLogic
    # force_field_logic: ForceFieldLogic
    # enabled_worlds: EnabledWorlds
    # start_world: StartWorld
    # last_world: LastWorld
    death_link: DeathLink
    enable_time_stars: EnableTimeStars
    enable_no_deaths_stars: EnableNoDeathsStars
    enable_collectible_stars: EnableCollectibleStars
    enable_challenge_stars: EnableChallengeStars
    enable_pogo_stars: EnablePogoStars
    enable_tiny_toy_stars: EnableTinyToyStars
    enable_jetpack_stars: EnableJetpackStars
    enable_chase_the_grade_stars: EnableChaseTheGradeStars
    enable_all_course_stars: EnableAllCourseStars
    enable_buddy_stars: EnableBuddyStars
    enable_buddy_chase_stars: EnableBuddyChaseStars
    
    
option_id_to_world_name: dict[int, str] = {
    WorldSelect.option_random_world: "Random",
    WorldSelect.option_gym_class: "Gym Class",
    WorldSelect.option_playground: "Playground",
    WorldSelect.option_school: "School",
    WorldSelect.option_wholesale: "Wholesale",
    WorldSelect.option_master_class: "Master Class",
    WorldSelect.option_basement: "Basement",
    WorldSelect.option_roccos_arcade: "Rocco's Arcade",
}

def get_enabled_world_names(world: HotLavaWorld) -> list[str]:
    # enabled_worlds: list[str] = []
    
    # for camel_case_name in world.options.enabled_worlds.value:
    #     game_world_name = next((key for key, value in game_world_dict.items() if value.camel_case_name == camel_case_name), None)
    #     enabled_worlds.append(game_world_name)
        
    # return enabled_worlds
    return ["Gym Class", "Playground", "School", "Wholesale", "Master Class", "Basement", "Rocco's Arcade"]