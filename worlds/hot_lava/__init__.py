import settings

from worlds.hot_lava.Regions import create_regions_for_all_worlds
from .Items import HotLavaItem, get_all_items_table, get_items_by_world
from .Locations import get_location_name_to_id_for_all
from .Options import HotLavaOptions
from BaseClasses import Tutorial, ItemClassification, Region
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
    item_name_to_id = {name: data.code for name, data in get_all_items_table().items() if data.code is not None}
    location_name_to_id = get_location_name_to_id_for_all()

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

        create_regions_for_all_worlds(self, menu_region)

    def create_item(self, name) -> HotLavaItem:
        data = get_all_items_table()[name]
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
        
        # TODO: random starting world?
        self.multiworld.push_precollected(self.create_item("World Unlock - Gym Class"))

        items_by_world = get_items_by_world()
        for world in items_by_world:
            for item_name in items_by_world[world]:
                # Don't add any pre-collected items to the pool
                if (not any(item.name == item_name for item in self.multiworld.precollected_items[self.player])):
                    item = self.create_item(item_name)
                    self.multiworld.itempool.append(item)

        # itempool and number of locations should match up.
        # If this is not the case we want to fill the itempool with junk.
        junk = self.get_total_locations() - len(self.multiworld.itempool)  # calculate this based on player options
        self.multiworld.itempool += [self.create_item("XP Shard") for _ in range(junk)]
        
    def get_total_locations(self) -> int:
        total_locations = 0
        for region in self.multiworld.regions:
            total_locations += len(region.locations)
        return total_locations

    def set_rules(self) -> None:
        #TODO
        self.multiworld.completion_condition[self.player] = lambda state: any(location.name == "Gym Class - Gym Jam - Complete the course" for location in state.locations_checked)