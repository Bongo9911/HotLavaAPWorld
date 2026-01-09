from typing import NamedTuple

from BaseClasses import Item, ItemClassification

class HotLavaItem(Item):
    game: str = "Hot Lava"

class HotLavaItemData(NamedTuple):
    code: int
    classification: ItemClassification = ItemClassification.progression

gym_class_item_data_table: dict[str, HotLavaItemData] = {
    "Gym Class - Back Hallway Force Field" : HotLavaItemData(100)
}

item_data_table: dict[str, HotLavaItemData] = {
    "XP Shard": HotLavaItemData(1, ItemClassification.filler),
    **gym_class_item_data_table
}