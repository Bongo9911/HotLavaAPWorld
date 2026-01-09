from typing import NamedTuple

from BaseClasses import Item, ItemClassification
from .Data import load_world_data

class HotLavaItem(Item):
    game: str = "Hot Lava"

class HotLavaItemData(NamedTuple):
    code: int
    classification: ItemClassification = ItemClassification.progression

filler_items: dict[str, HotLavaItemData] = {
    "XP Shard": HotLavaItemData(1, ItemClassification.filler),
}

items_by_world: dict[str, dict[str, HotLavaItemData]] = None
item_data_table: dict[str, HotLavaItemData] = None

def build_locations_from_json():    
    worlds = load_world_data()

    items_by_world = {}
    
    worldIdOffset = 100
    for world in worlds:
        world_table: dict[str, HotLavaItemData] = {}
        items_by_world[world["Name"]] = world_table
        
        # TODO World Unlock item
        itemIdOffset = 1
        for index, forceField in enumerate(world["ForceFields"]):
            name = world["Name"] + " - Force Field Deactivate - " + forceField["Name"]
            id = worldIdOffset + itemIdOffset + index
            world_table[name] = HotLavaItemData(id, ItemClassification.progression)
            
        worldIdOffset += 100
        
    return items_by_world
            
def get_items_by_world():
    global items_by_world
    
    if(items_by_world == None):
        items_by_world = build_locations_from_json()
    
    return items_by_world

def get_all_items_table() -> dict[str, HotLavaItemData]:
    global items_table
    
    if (item_data_table == None):
        items_by_world = get_items_by_world()
        
        items_table = {**filler_items}
        for world in items_by_world:
            items_table.update(items_by_world[world])
        
    return items_table