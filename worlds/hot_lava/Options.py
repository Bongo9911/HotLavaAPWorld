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
    
    option_random = 0
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

@dataclass
class HotLavaOptions(PerGameCommonOptions):
    world_unlock_logic: WorldUnlockLogic
    force_field_logic: ForceFieldLogic
    enabled_worlds: EnabledWorlds
    start_world: StartWorld
    last_world: LastWorld
    death_link: DeathLink
    
    
option_id_to_world_name: dict[int, str] = {
    WorldSelect.option_random: "Random",
    WorldSelect.option_gym_class: "Gym Class",
    WorldSelect.option_playground: "Playground",
    WorldSelect.option_school: "School",
    WorldSelect.option_wholesale: "Wholesale",
    WorldSelect.option_master_class: "Master Class",
    WorldSelect.option_basement: "Basement",
    WorldSelect.option_roccos_arcade: "Rocco's Arcade",
}

def get_enabled_world_names(world: HotLavaWorld):
    enabled_worlds: list[str] = []
    
    for camel_case_name in world.options.enabled_worlds.value:
        game_world_name = next((key for key, value in game_world_dict.items() if value.camel_case_name == camel_case_name), None)
        enabled_worlds.append(game_world_name)
        
    return enabled_worlds