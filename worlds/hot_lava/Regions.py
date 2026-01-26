from typing import Callable, Optional

from ..AutoWorld import World
from .Locations import HotLavaLocation, HotLavaLocationInfo, get_locations_info_for_course
from .CourseType import CourseType
from .StarType import StarType
from BaseClasses import CollectionState, LocationProgressType, Region

def create_regions_for_all_worlds(world: World, menu_region: Region) -> None:
    create_gym_class_regions(world, menu_region)
    create_playground_regions(world, menu_region)
    create_school_regions(world, menu_region)
    create_wholesale_regions(world, menu_region)

def create_gym_class_regions(world: World, menu_region: Region) -> None:
    world_name = "Gym Class"
    buddy_region_base = "Side Entrance"
    buddy_region_name = world_name + " - " + buddy_region_base
    
    gym_class_spawn_region = create_region_for_world(world, world_name, "Spawn")
    menu_region.connect(gym_class_spawn_region, rule=lambda collection: collection.has("World Unlock - Gym Class", world.player)) 
    
    office_hallway_region = create_region_for_world(world, world_name, "Office Hallway")
    gym_class_spawn_region.connect(office_hallway_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Gym/Office Hallway"), world.player))
    
    janitors_closet_region = create_region_for_world(world, world_name, "Janitor's Closet")
    office_hallway_region.connect(janitors_closet_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Office Hallway/Janitor's Closet"), world.player))
    
    back_hallway_region = create_region_for_world(world, world_name, "Back Hallway")
    office_hallway_region.connect(back_hallway_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Office Hallway/Back Hallway"), world.player))
    gym_class_spawn_region.connect(back_hallway_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Computer Lab Hallway/Back Hallway"), world.player))
    
    side_entrance_region = create_region_for_world(world, world_name, "Side Entrance")
    back_hallway_region.connect(side_entrance_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Back Hallway/Side Entrance"), world.player))
    
    create_region_for_course(world, world_name, "Gym Jam", gym_class_spawn_region, buddy_region_name)
    create_region_for_course(world, world_name, "Trampoline Trouble", gym_class_spawn_region, buddy_region_name)
    create_region_for_course(world, world_name, "Livin' on the Ledge", office_hallway_region, buddy_region_name)
    create_region_for_course(world, world_name, "Surfing Surfaces", janitors_closet_region, buddy_region_name)
    create_region_for_course(world, world_name, "Pole Vault", back_hallway_region, buddy_region_name)
    create_region_for_course(world, world_name, "Chase Your Sister", back_hallway_region, buddy_region_name)
    
    create_region_for_course(world, world_name, "Tiny Toy Trial", office_hallway_region)
    create_region_for_course(world, world_name, "Pogo Trial", janitors_closet_region)
    create_region_for_course(world, world_name, "Jetpack Trial", back_hallway_region)
    create_region_for_course(world, world_name, "All Course Marathon", side_entrance_region)
    
    
def create_playground_regions(world: World, menu_region: Region) -> None:
    world_name = "Playground"
    buddy_region_base = "Sports Day Side"
    buddy_region_name = world_name + " - " + buddy_region_base
    
    playground_spawn_region = create_region_for_world(world, world_name, "Spawn")
    menu_region.connect(playground_spawn_region, rule=lambda collection: collection.has("World Unlock - Playground", world.player))
    
    basketball_courts_region = create_region_for_world(world, world_name, "Basketball Courts")
    playground_spawn_region.connect(basketball_courts_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Spawn/Basketball Courts"), world.player))
    
    sports_day_side_region = create_region_for_world(world, world_name, "Sports Day Side")
    basketball_courts_region.connect(sports_day_side_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Basketball Courts/Sports Day Side"), world.player))
    
    create_region_for_course(world, world_name, "Recess", playground_spawn_region, buddy_region_name)
    create_region_for_course(world, world_name, "Big Kids Side", basketball_courts_region, buddy_region_name)
    create_region_for_course(world, world_name, "Bouncy Castle", sports_day_side_region, buddy_region_name)
    create_region_for_course(world, world_name, "Back to Class", sports_day_side_region, buddy_region_name)
    create_region_for_course(world, world_name, "Sports Day", sports_day_side_region, buddy_region_name)
    create_region_for_course(world, world_name, "Chase the Big Kid", sports_day_side_region, buddy_region_name)
    
    create_region_for_course(world, world_name, "Jetpack Trial", playground_spawn_region)
    create_region_for_course(world, world_name, "Pogo Trial 1", basketball_courts_region)
    create_region_for_course(world, world_name, "Tiny Toy Trial 1", basketball_courts_region)
    create_region_for_course(world, world_name, "Pogo Trial 2", sports_day_side_region)
    create_region_for_course(world, world_name, "Tiny Toy Trial 2", sports_day_side_region)
    create_region_for_course(world, world_name, "Chase the Grade", sports_day_side_region)
    create_region_for_course(world, world_name, "All Course Marathon", basketball_courts_region)
    
def create_school_regions(world: World, menu_region: Region) -> None:
    world_name = "School"
    buddy_region_base = "Cafeteria/Social Studies Hallway"
    buddy_region_name = world_name + " - " + buddy_region_base
    
    atrium_region = create_region_for_world(world, world_name, "Atrium")
    menu_region.connect(atrium_region, rule=lambda collection: collection.has("World Unlock - School", world.player))
    
    teachers_lounge_region = create_region_for_world(world, world_name, "Teacher's Lounge")
    atrium_region.connect(teachers_lounge_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "English Hallway/Teacher's Lounge Hallway"), world.player))
    
    courtyard_region = create_region_for_world(world, world_name, "Courtyard")
    teachers_lounge_region.connect(courtyard_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Teacher's Lounge/Courtyard"), world.player))
    
    art_hallway_gym_region = create_region_for_world(world, world_name, "Art Hallway/Gym")
    teachers_lounge_region.connect(art_hallway_gym_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Teacher's Lounge Hallway/Art Hallway"), world.player))
    
    cafeteria_social_studies_region = create_region_for_world(world, world_name, buddy_region_base)
    art_hallway_gym_region.connect(cafeteria_social_studies_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Social Studies Hallway/Art Hallway"), world.player))
    atrium_region.connect(cafeteria_social_studies_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Atrium/Cafeteria"), world.player) or 
                          collection.has(get_forcefield_name(world_name, "Atrium/Social Studies Hallway"), world.player))
    
    social_studies_region = create_region_for_world(world, world_name, "Social Studies Class")
    cafeteria_social_studies_region.connect(social_studies_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Social Studies Class Left"), world.player) or 
                        collection.has(get_forcefield_name(world_name, "Social Studies Class Right"), world.player))
    
    art_class_region = create_region_for_world(world, world_name, "Art Class")
    art_hallway_gym_region.connect(art_class_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Art Hallway/Art Class"), world.player))
        
    art_closet_region = create_region_for_world(world, world_name, "Art Closet")
    art_class_region.connect(art_closet_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Art Closet/Art Class"), world.player))
    
    science_lab_region = create_region_for_world(world, world_name, "Science Lab")
    art_hallway_gym_region.connect(science_lab_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Gym Hallway/Science Lab"), world.player))
    art_closet_region.connect(science_lab_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Science Lab/Art Closet"), world.player))
        
    computer_lab_region = create_region_for_world(world, world_name, "Computer Lab")
    art_hallway_gym_region.connect(computer_lab_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Gym Hallway/Computer Lab"), world.player))
    
    create_region_for_course(world, world_name, "ABCs and 123s", atrium_region, buddy_region_name)
    create_region_for_course(world, world_name, "Middle School Mischief", teachers_lounge_region, buddy_region_name)
    create_region_for_course(world, world_name, "Repeat the Grade", art_hallway_gym_region, buddy_region_name)
    create_region_for_course(world, world_name, "Senior Trip", courtyard_region, buddy_region_name)
    create_region_for_course(world, world_name, "Freshman Frenzy", computer_lab_region, buddy_region_name)
    create_region_for_course(world, world_name, "Chase Your Sister", art_hallway_gym_region, buddy_region_name)
    
    create_region_for_course(world, world_name, "Pogo Trial 1", teachers_lounge_region)
    create_region_for_course(world, world_name, "Pogo Trial 2", art_hallway_gym_region)
    create_region_for_course(world, world_name, "Pogo Trial 3", social_studies_region)
    create_region_for_course(world, world_name, "Tiny Toy Trial", teachers_lounge_region)
    create_region_for_course(world, world_name, "Jetpack Trial", cafeteria_social_studies_region)
    create_region_for_course(world, world_name, "Chase the Grade", art_class_region)
    create_region_for_course(world, world_name, "All Course Marathon", art_closet_region)
    
def create_wholesale_regions(world: World, menu_region: Region) -> None:
    world_name = "Wholesale"
    buddy_region_base = "Shopping Area"
    buddy_region_name = world_name + " - " + buddy_region_base
    
    employee_hallway_region = create_region_for_world(world, world_name, "Employee Hallway")
    menu_region.connect(employee_hallway_region, rule=lambda collection: collection.has("World Unlock - " + world_name, world.player))
    
    breakroom_region = create_region_for_world(world, world_name, "Breakroom")
    employee_hallway_region.connect(breakroom_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Employee Hallway/Breakroom"), world.player))
    
    janitors_closet_region = create_region_for_world(world, world_name, "Janitor's Closet")
    employee_hallway_region.connect(janitors_closet_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Employee Hallway/Janitor's Closet"), world.player))
    
    checkout_region = create_region_for_world(world, world_name, "Checkout")
    employee_hallway_region.connect(checkout_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Employee Hallway/Checkout"), world.player))
    
    cart_storage_region = create_region_for_world(world, world_name, "Cart Storage")
    checkout_region.connect(cart_storage_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Checkout/Cart Storage"), world.player))
    
    shopping_area_region = create_region_for_world(world, world_name, buddy_region_base)
    checkout_region.connect(shopping_area_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Checkout/Shopping Area"), world.player))
    
    under_shelves_region = create_region_for_world(world, world_name, "Under the Shelves")
    shopping_area_region.connect(under_shelves_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Under the Shelves"), world.player))
    
    create_region_for_course(world, world_name, "To the Top", employee_hallway_region, buddy_region_name)
    create_region_for_course(world, world_name, "Duct and Cover", checkout_region, buddy_region_name)
    create_region_for_course(world, world_name, "Meat Market", shopping_area_region, buddy_region_name)
    create_region_for_course(world, world_name, "Returns", checkout_region, buddy_region_name)
    create_region_for_course(world, world_name, "Meat Grinder", checkout_region, buddy_region_name)
    create_region_for_course(world, world_name, "Chase Through the Store", shopping_area_region, buddy_region_name)
        
    create_region_for_course(world, world_name, "Pogo Trial 1", checkout_region)
    create_region_for_course(world, world_name, "Pogo Trial 2", cart_storage_region)
    create_region_for_course(world, world_name, "Pogo Trial 3", janitors_closet_region)
    create_region_for_course(world, world_name, "Tiny Toy Trial", shopping_area_region)
    create_region_for_course(world, world_name, "Jetpack Trial", shopping_area_region)
    create_region_for_course(world, world_name, "Chase the Grade", breakroom_region)
    create_region_for_course(world, world_name, "All Course Marathon", under_shelves_region)
    
    
def create_region_for_world(world: World, world_name: str, region_name: str) -> Region:
    region = Region(world_name + " - " + region_name, world.player, world.multiworld)
    world.multiworld.regions.append(region)
    return region
    
def create_region_for_course(world: World, world_name: str, course_name: str, parent_region: Region,
                                buddy_region_name = None,
                                rule: Optional[Callable[[CollectionState], bool]] = None) -> Region:
    region = Region(world_name + " - " + course_name, world.player, world.multiworld)
    locationsInfo = get_locations_info_for_course(world_name, course_name)
    for locationInfo in locationsInfo:
        if(locationInfo.starType == StarType.Buddy and buddy_region_name != None):
            buddy_region = Region(world_name + " - " + course_name + " - Buddy", world.player, world.multiworld)
            buddy_region.locations.append(build_location(world, buddy_region, locationInfo))
            world.multiworld.regions.append(buddy_region)
            region.connect(buddy_region, rule=lambda collection: collection.can_reach_region(buddy_region_name, world.player))
        else:
            region.locations.append(build_location(world, region, locationInfo))
        
    world.multiworld.regions.append(region)
    
    parent_region.connect(region, rule=rule)
    return region

def build_location(world: World, region: Region, locationInfo: HotLavaLocationInfo) -> HotLavaLocation:
    location = HotLavaLocation(world.player, locationInfo.name, locationInfo.id, region)
    
    #TODO: allow the progress type to be configurable in options
    if (locationInfo.starType == StarType.CourseComplete or locationInfo.courseType == CourseType.Pogo or locationInfo.courseType == CourseType.TinyToy or locationInfo.courseType == CourseType.Jetpack or locationInfo.courseType == CourseType.Chase):
        location.progress_type = LocationProgressType.PRIORITY
    elif (locationInfo.starType == StarType.Buddy or locationInfo.courseType == CourseType.AllCourseMarathon):
        location.progress_type = LocationProgressType.EXCLUDED
    else:
        location.progress_type = LocationProgressType.DEFAULT
        
    return location

def get_forcefield_name(world_name, forcefield_name):
    return world_name + " - Force Field Deactivate - " + forcefield_name