from typing import Callable, Optional

from ..AutoWorld import World
from .Locations import HotLavaLocation, HotLavaLocationInfo, get_locations_info_for_course
from BaseClasses import CollectionState, Region

def create_regions_for_all_worlds(world: World, menu_region: Region) -> None:
    create_gym_class_regions(world, menu_region)
    create_playground_regions(world, menu_region)

def create_gym_class_regions(world: World, menu_region: Region) -> None:
    world_name = "Gym Class"
    
    gym_class_spawn_region = create_region_for_world(world, world_name, "Spawn")
    menu_region.connect(gym_class_spawn_region, rule=lambda collection: collection.has("World Unlock - Gym Class", world.player)) 
    
    office_hallway_region = create_region_for_world(world, world_name, "Office Hallway")
    gym_class_spawn_region.connect(office_hallway_region, rule=lambda collection: collection.has("Gym Class - Force Field Deactivate - Gym/Office Hallway", world.player))
    
    janitors_closet_region = create_region_for_world(world, world_name, "Janitor's Closet")
    office_hallway_region.connect(janitors_closet_region, rule=lambda collection: collection.has("Gym Class - Force Field Deactivate - Office Hallway/Janitor's Closet", world.player))
    
    back_hallway_region = create_region_for_world(world, world_name, "Back Hallway")
    office_hallway_region.connect(back_hallway_region, rule=lambda collection: collection.has("Gym Class - Force Field Deactivate - Office Hallway/Back Hallway", world.player))
    gym_class_spawn_region.connect(back_hallway_region, rule=lambda collection: collection.has("Gym Class - Force Field Deactivate - Computer Lab Hallway/Back Hallway", world.player))
    
    side_entrance_region = create_region_for_world(world, world_name, "Side Entrance")
    back_hallway_region.connect(side_entrance_region, rule=lambda collection: collection.has("Gym Class - Force Field Deactivate - Back Hallway/Side Entrance", world.player))
    
    create_region_for_course(world, world_name, "Gym Jam", gym_class_spawn_region)
    create_region_for_course(world, world_name, "Trampoline Trouble", gym_class_spawn_region)
    create_region_for_course(world, world_name, "Livin' on the Ledge", office_hallway_region)
    create_region_for_course(world, world_name, "Surfing Surfaces", janitors_closet_region)
    create_region_for_course(world, world_name, "Pole Vault", back_hallway_region)
    create_region_for_course(world, world_name, "Chase Your Sister", back_hallway_region)
    
    create_region_for_course(world, world_name, "Tiny Toy Trial", office_hallway_region)
    create_region_for_course(world, world_name, "Pogo Trial", janitors_closet_region)
    create_region_for_course(world, world_name, "Jetpack Trial", back_hallway_region)
    create_region_for_course(world, world_name, "All Course Marathon", side_entrance_region)
    
    
def create_playground_regions(world: World, menu_region: Region) -> None:
    world_name = "Playground"
    
    playground_spawn_region = create_region_for_world(world, world_name, "Spawn")
    menu_region.connect(playground_spawn_region, rule=lambda collection: collection.has("World Unlock - Playground", world.player))
    
    basketball_courts_region = create_region_for_world(world, world_name, "Basketball Courts")
    playground_spawn_region.connect(basketball_courts_region) #TODO forcefield rule
    
    sports_day_side_region = create_region_for_world(world, world_name, "Sports Day Side")
    basketball_courts_region.connect(sports_day_side_region) #TODO force field
    
    create_region_for_course(world, world_name, "Recess", playground_spawn_region)
    create_region_for_course(world, world_name, "Big Kids Side", basketball_courts_region)
    create_region_for_course(world, world_name, "Bouncy Castle", sports_day_side_region)
    create_region_for_course(world, world_name, "Back to Class", sports_day_side_region)
    create_region_for_course(world, world_name, "Sports Day", sports_day_side_region)
    create_region_for_course(world, world_name, "Chase the Big Kid", sports_day_side_region)
    
    create_region_for_course(world, world_name, "Jetpack Trial", playground_spawn_region)
    create_region_for_course(world, world_name, "Pogo Trial 1", basketball_courts_region)
    create_region_for_course(world, world_name, "Tiny Toy Trial 1", basketball_courts_region)
    create_region_for_course(world, world_name, "Pogo Trial 2", sports_day_side_region)
    create_region_for_course(world, world_name, "Tiny Toy Trial 2", sports_day_side_region)
    create_region_for_course(world, world_name, "Chase the Grade", sports_day_side_region)
    create_region_for_course(world, world_name, "All Course Marathon", basketball_courts_region)
    
    
def create_region_for_world(world: World, world_name: str, region_name: str) -> Region:
    region = Region(world_name + " - " + region_name, world.player, world.multiworld)
    world.multiworld.regions.append(region)
    return region
    
def create_region_for_course(world: World, world_name: str, course_name: str, parent_region: Region, 
                                rule: Optional[Callable[[CollectionState], bool]] = None) -> Region:
    region = Region(world_name + " - " + course_name , world.player, world.multiworld)
    locationsInfo = get_locations_info_for_course(world_name, course_name)
    for locationInfo in locationsInfo:
        region.locations.append(build_location(world, region, locationInfo))
        
    world.multiworld.regions.append(region)
    
    parent_region.connect(region, rule=rule)
    return region

def build_location(world: World, region: Region, locationInfo: HotLavaLocationInfo) -> HotLavaLocation:
    location = HotLavaLocation(world.player, locationInfo.name, locationInfo.id, region)
    location.progress_type = locationInfo.progressType
    return location