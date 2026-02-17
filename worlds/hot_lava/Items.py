from __future__ import annotations

import math
import random
from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Item, ItemClassification
from .Options import get_enabled_world_names, option_id_to_world_name
from .Data import game_world_dict

if TYPE_CHECKING:
    from .World import HotLavaWorld

class HotLavaItem(Item):
    game: str = "Hot Lava"

class HotLavaItemData:
    code: int
    classification: ItemClassification = ItemClassification.progression
    
    def __init__(self, code, classification):
        self.code = code
        self.classification = classification
    
class HotLavaWorldUnlockItemData(HotLavaItemData):
    world_name: str
    
    def __init__(self, code, world_name, classification):
        super().__init__(code, classification)
        self.world_name = world_name
        
class HotLavaForceFieldItemData(HotLavaItemData):
    world_name: str
    
    def __init__(self, code, world_name, classification):
        super().__init__(code, classification)
        self.world_name = world_name

filler_items: dict[str, HotLavaItemData] = {
    "XP Shard": HotLavaItemData(1, ItemClassification.filler),
    "Star": HotLavaItemData(2, ItemClassification.progression_skip_balancing),
}

world_unlock_items: dict[str, HotLavaWorldUnlockItemData] = None
force_field_items: dict[str, HotLavaForceFieldItemData] = None

items_by_world: dict[str, dict[str, HotLavaItemData]] = None
item_data_table: dict[str, HotLavaItemData] = None

def build_items():
    global world_unlock_items
    world_unlock_items = {}
    
    for world in game_world_dict.values():
        world_unlock_name = "World Unlock - " + world.name
        world_unlock_items[world_unlock_name] = HotLavaWorldUnlockItemData(world.item_id, world.name, ItemClassification.progression)
        
        for force_field in world.force_fields:
            force_field_item_name = get_forcefield_name(world.name, force_field.name)
            force_field_items[force_field_item_name] = HotLavaForceFieldItemData(force_field.item_id, world.name, ItemClassification.progression)
            
def get_forcefield_name(world_name, forcefield_name):
    return world_name + " - Force Field Deactivate - " + forcefield_name

def get_all_items_table() -> dict[str, HotLavaItemData]:
    global item_data_table
    
    if (item_data_table == None):
        # items_by_world = get_items_by_world()
        build_items()
        
        item_data_table = {**filler_items, **world_unlock_items}
        # for world in items_by_world:
        #     item_data_table.update(items_by_world[world])
        
    return item_data_table

def create_all_items(world: HotLavaWorld):
    enabled_worlds: list[str] = get_enabled_world_names(world)
    
    if (world.options.world_unlock_logic.value == world.options.world_unlock_logic.option_world_item):
        world_unlocks_to_add: list[str] = enabled_worlds.copy()
        start_world_name: str = option_id_to_world_name[world.options.start_world.value]
        
        if(start_world_name == "Random"):
            start_world_name = random.choice(world_unlocks_to_add)
        elif start_world_name not in world_unlocks_to_add:
            # TODO ERROR
            pass
        
        world_unlocks_to_add.remove(start_world_name)
        
        world.multiworld.push_precollected(world.create_item("World Unlock - " + start_world_name))
        
        for world_name in world_unlocks_to_add:
            item_name = next((key for key, value in world_unlock_items.items() if value.world_name == world_name), None)
            item = world.create_item(item_name)
            world.multiworld.itempool.append(item)
            
    if (world.options.force_field_logic.value == world.options.force_field_logic.option_force_field_item):
        force_fields = [key for key, value in force_field_items.items() if value.world_name in enabled_worlds]
        
        for force_field_name in force_fields:
            item = world.create_item(force_field_name)
            world.multiworld.itempool.append(item)
            
    junk = world.get_total_locations() - len(world.multiworld.itempool)  # calculate this based on player options
    
    if (world.options.world_unlock_logic.value == world.options.world_unlock_logic.option_star_items):
        star_junk = math.ceil(junk * .75)
        xp_junk = junk - star_junk
        world.multiworld.itempool += [world.create_item("Star") for _ in range(star_junk)]
    else:
        xp_junk = junk
    
    world.multiworld.itempool += [world.create_item("XP Shard") for _ in range(xp_junk)]