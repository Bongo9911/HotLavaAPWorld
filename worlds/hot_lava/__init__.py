import settings
import typing
from .Items import HotLavaItem, item_data_table, gym_class_item_data_table
from .Locations import HotLavaLocation, get_locations_for_world
from .Options import HotLavaOptions
from BaseClasses import Item, Tutorial, ItemClassification, Region
from ..AutoWorld import World, WebWorld

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

# class HotLavaSettings(settings.Group):
#     class RomFile(settings.SNESRomPath):
#         """Insert help text for host.yaml here."""

#     rom_file: RomFile = RomFile("MyGame.sfc")

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
    item_name_to_id = {name: data.code for name, data in item_data_table.items() if data.code is not None}
    location_name_to_id = get_locations_for_world("Gym Class")

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = {
        # "weapons": {"sword", "lance"},
    }

    def create_regions(self) -> None:
        # Add regions to the multiworld. One of them must use the origin_region_name as its name ("Menu" by default).
        # Arguments to Region() are name, player, multiworld, and optionally hint_text
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)  # or use += [menu_region...]

        gym_class_spawn_region = Region("Gym Class - Spawn", self.player, self.multiworld)
        gym_class_spawn_region.add_locations(get_locations_for_world("Gym Class"), HotLavaLocation)
        # or 
        # main_region.locations = \
        #   [MyGameLocation(self.player, location_name, self.location_name_to_id[location_name], main_region]
        self.multiworld.regions.append(gym_class_spawn_region)

        # if entrances are not randomized, they should be connected here, otherwise they can also be connected at a later stage
        # create Entrances and connect the Regions
        menu_region.connect(gym_class_spawn_region)  # connects the "Menu" and "Main Area", can also pass a rule


    def create_item(self, name) -> HotLavaItem:
        data = item_data_table[name]
        item = HotLavaItem(name, data.classification, data.code, self.player)

        return item
    
    def create_event(self, event: str) -> HotLavaItem:
        # while we are at it, we can also add a helper to create events
        return HotLavaItem(event, ItemClassification.progression, None, self.player)
    
    def create_items(self) -> None:
        # Add items to the Multiworld.
        # If there are two of the same item, the item has to be twice in the pool.
        # Which items are added to the pool may depend on player options, e.g. custom win condition like triforce hunt.
        # Having an item in the start inventory won't remove it from the pool.
        # If you want to do that, use start_inventory_from_pool

        for item_name in gym_class_item_data_table:
            item = self.create_item(item_name)
            self.multiworld.itempool.append(item)

        # TODO
        # itempool and number of locations should match up.
        # If this is not the case we want to fill the itempool with junk.
        junk = len(self.location_name_to_id) - len(self.multiworld.itempool)  # calculate this based on player options
        self.multiworld.itempool += [self.create_item("XP Shard") for _ in range(junk)]

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: any(location.name == "Gym Class - Gym Jam - Complete the course" for location in state.locations_checked)