import math
import random
from typing import Any
import settings

from worlds.generic.Rules import set_rule
from .Regions import create_regions_for_all_worlds
from .Items import HotLavaItem, create_all_items, get_all_items_table
from .Locations import build_location_name_groups, get_all_location_infos, get_location_name_to_id_for_all, get_locations_info_for_world
from .Options import HotLavaOptions
from .StarType import StarType
from BaseClasses import CollectionState, Tutorial, ItemClassification, Region
from ..AutoWorld import World
from .Rules import set_all_rules

class HotLavaWorld(World):
    """Hot Lava is 3D parkour-platformer game developed by Klei Entertainment inspired by the classic kids' game 'The Floor is Lava'"""
    game = "Hot Lava" # name of the game/world
    options_dataclass = HotLavaOptions # options the player can set
    options: HotLavaOptions # typing hints for option results
    # settings: typing.ClassVar[HotLavaSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {name: data.code for name, data in get_all_items_table().items() if data.code is not None}
    location_name_to_id = get_location_name_to_id_for_all()

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = {
        "Worlds": {"World Unlock - Gym Class", "World Unlock - Playground", "World Unlock - School", "World Unlock - Wholesale", "World Unlock - Master Class", "World Unlock - Basement", "World Unlock - Rocco's Arcade"},
        "Standard Abilities": {"Crouch", "Grab", "Surf", "Wall Jump", "Swing", "Climb"},
        "Special Abilities": {"Double Jump", "Boost Jump", "Slide Jump", "Vault Jump"},
        "Trials": {"Pogo", "Tiny Toy", "Jetpack"},
    }
    
    location_name_groups = build_location_name_groups()
    
    stars_per_world: dict[str, int] = {}

    def create_regions(self) -> None:
        # Add regions to the multiworld. One of them must use the origin_region_name as its name ("Menu" by default).
        # Arguments to Region() are name, player, multiworld, and optionally hint_text
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)  # or use += [menu_region...]

        create_regions_for_all_worlds(self, menu_region)

    def create_item(self, name) -> HotLavaItem:
        data = get_all_items_table()[name]
        item = HotLavaItem(name, data.classification, data.code, self.player)

        return item
    
    def get_filler_item_name(self):
        # TODO: Should this randomly return star or XP Shard?
        return "XP Shard"
    
    def create_event(self, event: str) -> HotLavaItem:
        # while we are at it, we can also add a helper to create events
        return HotLavaItem(event, ItemClassification.progression, None, self.player)
    
    def create_items(self) -> None:
        # Add items to the Multiworld.
        # If there are two of the same item, the item has to be twice in the pool.
        # Which items are added to the pool may depend on player options, e.g. custom win condition like triforce hunt.
        # Having an item in the start inventory won't remove it from the pool.
        # If you want to do that, use start_inventory_from_pool
        
        create_all_items(self)
        
    def get_total_locations(self) -> int:
        return len(self.multiworld.get_locations(self.player))

    def set_rules(self) -> None:
        set_all_rules(self)
        
    def fill_slot_data(self) -> dict[str, Any]: 
        return self.options.as_dict(
            "death_link"
        )
        
        # return self.options.as_dict(
        #     "world_unlock_logic", "force_field_logic", "enabled_worlds", "start_world", "last_world", "death_link"
        # )
        
        # slot_data: dict[str, Any] = {}
        
        # # slot_data["stars_per_world"] = self.stars_per_world
        
        # return slot_data