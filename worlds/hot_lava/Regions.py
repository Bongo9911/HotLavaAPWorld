from __future__ import annotations

from typing import Callable, Optional, TYPE_CHECKING

from worlds.generic.Rules import add_rule

from .Data import GameCourseInfo, GameStarInfo, game_world_dict
from .Locations import HotLavaLocation, HotLavaLocationInfo, get_locations_info_for_course
from .CourseType import CourseType
from .StarType import StarType
from BaseClasses import CollectionState, Entrance, LocationProgressType, MultiWorld, Region

if TYPE_CHECKING:
    from .World import HotLavaWorld

def create_regions_for_all_worlds(world: HotLavaWorld, menu_region: Region) -> None:
    create_intro_regions(world, menu_region)
    create_gym_class_regions(world, menu_region)
    create_playground_regions(world, menu_region)
    create_school_regions(world, menu_region)
    create_wholesale_regions(world, menu_region)
    create_master_class_regions(world, menu_region)
    create_basement_regions(world, menu_region)
    create_roccos_arcade_regions(world, menu_region)
    
def create_intro_regions(world: HotLavaWorld, menu_region: Region) -> None:
    world_name = "Intro"
    world_region = create_world_region(world, menu_region, world_name)
    
    location = HotLavaLocation(world.player, "Intro - Complete the Intro.", 1, world_region)
    world_region.locations.append(location)
    location.progress_type = LocationProgressType.PRIORITY

def create_gym_class_regions(world: HotLavaWorld, menu_region: Region) -> None:
    world_name = "Gym Class"
    buddy_region_base = "Side Entrance"
    buddy_region_name = world_name + " - " + buddy_region_base
    
    world_region = create_world_region(world, menu_region, world_name)
    
    gym_class_spawn_region = create_region_for_world(world, world_name, "Spawn")
    world_region.connect(gym_class_spawn_region) 
    # menu_region.connect(gym_class_spawn_region, rule=lambda collection: collection.has("World Unlock - Gym Class", world.player)) 
    
    office_hallway_region = create_region_for_world(world, world_name, "Office Hallway")
    # gym_class_spawn_region.connect(office_hallway_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Gym/Office Hallway"), world.player))
    
    janitors_closet_region = create_region_for_world(world, world_name, "Janitor's Closet")
    # office_hallway_region.connect(janitors_closet_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Office Hallway/Janitor's Closet"), world.player))
    
    back_hallway_region = create_region_for_world(world, world_name, "Back Hallway")
    # office_hallway_region.connect(back_hallway_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Office Hallway/Back Hallway"), world.player))
    # gym_class_spawn_region.connect(back_hallway_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Computer Lab Hallway/Back Hallway"), world.player))
    
    side_entrance_region = create_region_for_world(world, world_name, "Side Entrance")
    # back_hallway_region.connect(side_entrance_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Back Hallway/Side Entrance"), world.player))
    
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
    
    
def create_playground_regions(world: HotLavaWorld, menu_region: Region) -> None:
    world_name = "Playground"
    buddy_region_base = "Sports Day Side"
    buddy_region_name = world_name + " - " + buddy_region_base
    
    world_region = create_world_region(world, menu_region, world_name)

    playground_spawn_region = create_region_for_world(world, world_name, "Spawn")
    world_region.connect(playground_spawn_region) 
    # menu_region.connect(playground_spawn_region, rule=lambda collection: collection.has("World Unlock - Playground", world.player))
    
    basketball_courts_region = create_region_for_world(world, world_name, "Basketball Courts")
    # playground_spawn_region.connect(basketball_courts_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Spawn/Basketball Courts"), world.player))
    
    sports_day_side_region = create_region_for_world(world, world_name, "Sports Day Side")
    # basketball_courts_region.connect(sports_day_side_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Basketball Courts/Sports Day Side"), world.player))
    
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
    
def create_school_regions(world: HotLavaWorld, menu_region: Region) -> None:
    world_name = "School"
    buddy_region_base = "Cafeteria"
    buddy_region_name = world_name + " - " + buddy_region_base
    
    world_region = create_world_region(world, menu_region, world_name)
    
    atrium_region = create_region_for_world(world, world_name, "Atrium")
    world_region.connect(atrium_region)
    # menu_region.connect(atrium_region, rule=lambda collection: collection.has("World Unlock - School", world.player))
    
    teachers_lounge_region = create_region_for_world(world, world_name, "Teacher's Lounge")
    # atrium_region.connect(teachers_lounge_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "English Hallway/Teacher's Lounge Hallway"), world.player))
    
    courtyard_region = create_region_for_world(world, world_name, "Courtyard")
    # teachers_lounge_region.connect(courtyard_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Teacher's Lounge/Courtyard"), world.player))
    
    art_hallway_region = create_region_for_world(world, world_name, "Art Hallway")
    # teachers_lounge_region.connect(art_hallway_gym_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Teacher's Lounge Hallway/Art Hallway"), world.player))
    
    gym_hallway_region = create_region_for_world(world, world_name, "Gym Hallway")
    # art_hallway_region.connect(gym_hallway_region)
    
    gym_region = create_region_for_world(world, world_name, "Gym")
    # gym_hallway_region.connect(gym_region)
    
    cafeteria_region = create_region_for_world(world, world_name, buddy_region_base)
    # atrium_region.connect(cafeteria_region)
    
    social_studies_hallway_region = create_region_for_world(world, world_name, "Social Studies Hallway")
    # atrium_region.connect(social_studies_hallway_region)
    # art_hallway_region.connect(social_studies_hallway_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Social Studies Hallway/Art Hallway"), world.player))
    
    social_studies_region = create_region_for_world(world, world_name, "Social Studies Class")
    # social_studies_hallway_region.connect(social_studies_region)
    
    art_class_region = create_region_for_world(world, world_name, "Art Class")
    # art_hallway_region.connect(art_class_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Art Hallway/Art Class"), world.player))
        
    art_closet_region = create_region_for_world(world, world_name, "Art Closet")
    # art_class_region.connect(art_closet_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Art Closet/Art Class"), world.player))
    
    science_lab_region = create_region_for_world(world, world_name, "Science Lab")
    # gym_hallway_region.connect(science_lab_region)
    # art_closet_region.connect(science_lab_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Science Lab/Art Closet"), world.player))
        
    computer_lab_region = create_region_for_world(world, world_name, "Computer Lab")
    # gym_hallway_region.connect(computer_lab_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Gym Hallway/Computer Lab"), world.player))
    
    create_region_for_course(world, world_name, "ABCs and 123s", atrium_region, buddy_region_name)
    create_region_for_course(world, world_name, "Middle School Mischief", teachers_lounge_region, buddy_region_name)
    create_region_for_course(world, world_name, "Repeat the Grade", gym_region, buddy_region_name)
    create_region_for_course(world, world_name, "Senior Trip", courtyard_region, buddy_region_name)
    create_region_for_course(world, world_name, "Freshman Frenzy", computer_lab_region, buddy_region_name)
    create_region_for_course(world, world_name, "Chase Your Sister", gym_region, buddy_region_name)
    
    create_region_for_course(world, world_name, "Pogo Trial 1", teachers_lounge_region)
    create_region_for_course(world, world_name, "Pogo Trial 2", art_hallway_region)
    create_region_for_course(world, world_name, "Pogo Trial 3", social_studies_region)
    create_region_for_course(world, world_name, "Tiny Toy Trial", teachers_lounge_region)
    create_region_for_course(world, world_name, "Jetpack Trial", cafeteria_region)
    create_region_for_course(world, world_name, "Chase the Grade", art_class_region)
    create_region_for_course(world, world_name, "All Course Marathon", art_closet_region)
    
def create_wholesale_regions(world: HotLavaWorld, menu_region: Region) -> None:
    world_name = "Wholesale"
    buddy_region_base = "Shopping Area"
    buddy_region_name = world_name + " - " + buddy_region_base
    
    world_region = create_world_region(world, menu_region, world_name)
    
    employee_hallway_region = create_region_for_world(world, world_name, "Employee Hallway")
    world_region.connect(employee_hallway_region)
    # menu_region.connect(employee_hallway_region, rule=lambda collection: collection.has("World Unlock - " + world_name, world.player))
    
    breakroom_region = create_region_for_world(world, world_name, "Breakroom")
    # employee_hallway_region.connect(breakroom_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Employee Hallway/Breakroom"), world.player))
    
    janitors_closet_region = create_region_for_world(world, world_name, "Janitor's Closet")
    # employee_hallway_region.connect(janitors_closet_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Employee Hallway/Janitor's Closet"), world.player))
    
    checkout_region = create_region_for_world(world, world_name, "Checkout")
    # employee_hallway_region.connect(checkout_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Employee Hallway/Checkout"), world.player))
    
    cart_storage_region = create_region_for_world(world, world_name, "Cart Storage")
    # checkout_region.connect(cart_storage_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Checkout/Cart Storage"), world.player))
    
    shopping_area_region = create_region_for_world(world, world_name, buddy_region_base)
    # checkout_region.connect(shopping_area_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Checkout/Shopping Area"), world.player))
    
    under_shelves_region = create_region_for_world(world, world_name, "Under the Shelves")
    # shopping_area_region.connect(under_shelves_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Under the Shelves"), world.player))
    
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
    
def create_master_class_regions(world: HotLavaWorld, menu_region: Region) -> None:
    world_name = "Master Class"
    
    world_region = create_world_region(world, menu_region, world_name)
    
    gym_region = create_region_for_world(world, world_name, "Gym")
    world_region.connect(gym_region)
    # menu_region.connect(gym_region, rule=lambda collection: collection.has("World Unlock - " + world_name, world.player))
    
    create_region_for_course(world, world_name, "Air Control Mastery", gym_region)
    create_region_for_course(world, world_name, "Wall Jump Mastery", gym_region)
    create_region_for_course(world, world_name, "Surf Mastery", gym_region)
    create_region_for_course(world, world_name, "Boosting Mastery", gym_region)
    create_region_for_course(world, world_name, "Wind Tunnel Mastery", gym_region)
    create_region_for_course(world, world_name, "Honors Gym Class", gym_region)
        
    create_region_for_course(world, world_name, "Pogo Trial", gym_region)
    create_region_for_course(world, world_name, "Tiny Toy Trial", gym_region)
    create_region_for_course(world, world_name, "Jetpack Trial", gym_region)
    create_region_for_course(world, world_name, "All Course Marathon", gym_region)
    
def create_basement_regions(world: HotLavaWorld, menu_region: Region) -> None:
    world_name = "Basement"
    buddy_region_base = "Den"
    buddy_region_name = world_name + " - " + buddy_region_base
    
    world_region = create_world_region(world, menu_region, world_name)
    
    foyer_region = create_region_for_world(world, world_name, "Foyer")
    world_region.connect(foyer_region) 
    # menu_region.connect(foyer_region, rule=lambda collection: collection.has("World Unlock - " + world_name, world.player)) 
    
    living_room_region = create_region_for_world(world, world_name, "Living Room")
    # foyer_region.connect(living_room_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Foyer/Living Room"), world.player))
    
    dining_room_region = create_region_for_world(world, world_name, "Dining Room")
    # foyer_region.connect(dining_room_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Foyer/Dining Room"), world.player))
    
    kitchen_region = create_region_for_world(world, world_name, "Kitchen")
    # dining_room_region.connect(kitchen_region)
    
    basement_region = create_region_for_world(world, world_name, "Basement Storage")
    # kitchen_region.connect(basement_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Kitchen/Basement Storage"), world.player))
    
    den_region = create_region_for_world(world, world_name, buddy_region_base)
    # basement_region.connect(den_region, rule=lambda collection: collection.has(get_forcefield_name(world_name, "Basement Storage/Den"), world.player))
    
    create_region_for_course(world, world_name, "Race to the Summit", foyer_region, buddy_region_name)
    create_region_for_course(world, world_name, "Lights Out", foyer_region, buddy_region_name)
    create_region_for_course(world, world_name, "Temple Sprint", living_room_region, buddy_region_name)
    create_region_for_course(world, world_name, "Fancy Footwork", foyer_region, buddy_region_name)
    create_region_for_course(world, world_name, "Minecart Carnage", basement_region, buddy_region_name)
    create_region_for_course(world, world_name, "Chase The Meaning", basement_region, buddy_region_name)
    
    create_region_for_course(world, world_name, "Pogo Trial", dining_room_region)
    create_region_for_course(world, world_name, "Tiny Toy Trial", basement_region)
    create_region_for_course(world, world_name, "Jetpack Trial", foyer_region)
    create_region_for_course(world, world_name, "All Course Marathon", den_region)
    
def create_roccos_arcade_regions(world: HotLavaWorld, menu_region: Region) -> None:
    world_name = "Rocco's Arcade"
    buddy_region_base = "Arcade Rafters"
    buddy_region_name = world_name + " - " + buddy_region_base
    
    world_region = create_world_region(world, menu_region, world_name)
    
    arcade_region = create_region_for_world(world, world_name, "Arcade")
    world_region.connect(arcade_region)
    # menu_region.connect(arcade_region, rule=lambda collection: collection.has("World Unlock - " + world_name, world.player))
    
    arcade_rafters_region = create_region_for_world(world, world_name, "Arcade Rafters")
    arcade_rafters_entrance = arcade_region.connect(arcade_rafters_region)
    add_rule(arcade_rafters_entrance, lambda state: state.has_all(["Climb", "Swing"], world.player))
    
    create_region_for_course(world, world_name, "Arcade Action", arcade_region, buddy_region_name)
    create_region_for_course(world, world_name, "Rocco's Rumpus Room", arcade_region, buddy_region_name)
    create_region_for_course(world, world_name, "Employees Only", arcade_region, buddy_region_name)
    create_region_for_course(world, world_name, "Storage Room Spree", arcade_region, buddy_region_name)
    create_region_for_course(world, world_name, "Birthday Blowout", arcade_region, buddy_region_name)
    create_region_for_course(world, world_name, "Chase to the Arcade", arcade_region, buddy_region_name)
    
    create_region_for_course(world, world_name, "Pogo Trial 1", arcade_region)
    create_region_for_course(world, world_name, "Pogo Trial 2", arcade_region)
    create_region_for_course(world, world_name, "Tiny Toy Trial 1", arcade_region)
    create_region_for_course(world, world_name, "Tiny Toy Trial 2", arcade_region)
    create_region_for_course(world, world_name, "Jetpack Trial", arcade_region)
    create_region_for_course(world, world_name, "All Course Marathon", arcade_region)

def create_world_region(world: HotLavaWorld, menu_region: Region, world_name: str):
    world_region = Region(world_name, world.player, world.multiworld)
    world.multiworld.regions.append(world_region)
    menu_region.connect(world_region, world_name + " Menu Item")
    return world_region

    
def create_region_for_world(world: HotLavaWorld, world_name: str, region_name: str) -> Region:
    region = Region(world_name + " - " + region_name, world.player, world.multiworld)
    world.multiworld.regions.append(region)
    return region
    
def create_region_for_course(world: HotLavaWorld, world_name: str, course_name: str, parent_region: Region,
                                buddy_region_name = None,
                                rule: Optional[Callable[[CollectionState], bool]] = None) -> Region:
    region = Region(world_name + " - " + course_name, world.player, world.multiworld)
    locationsInfo = get_locations_info_for_course(world_name, course_name)
    
    for locationInfo in locationsInfo:
        if (not is_location_enabled(world, locationInfo)):
            continue
        
        if ((locationInfo.star_type == StarType.Buddy or locationInfo.star_type == StarType.BuddyChase) and buddy_region_name != None):
            buddy_region = Region(world_name + " - " + course_name + " - Buddy", world.player, world.multiworld)
            location = build_location(world, buddy_region, locationInfo)
            add_rule(location, lambda state: state.has_all({"Grab"}, world.player))
            buddy_region.locations.append(location)
            world.multiworld.regions.append(buddy_region)
            region.connect(buddy_region, rule=lambda collection: collection.can_reach_region(buddy_region_name, world.player))
        else:
            location = build_location(world, region, locationInfo)
            region.locations.append(location)
            
        if (locationInfo.course_type == CourseType.Pogo):
            add_rule(location, lambda state: state.has("Pogo", world.player))
        elif (locationInfo.course_type == CourseType.TinyToy):
            add_rule(location, lambda state: state.has("Tiny Toy", world.player))
        elif (locationInfo.course_type == CourseType.Jetpack):
            add_rule(location, lambda state: state.has("Jetpack", world.player))
            
        if (locationInfo.required_abilities != None):
            add_rule(location, lambda state, required_abilities=locationInfo.required_abilities: all(
                any(evaluate_has_ability(state, ability, world.player) for ability in or_group)
                for or_group in required_abilities
            ))            
        
    world.multiworld.regions.append(region)
    
    parent_region.connect(region, rule=rule)
    return region

def is_location_enabled(world: HotLavaWorld, locationInfo: HotLavaLocationInfo):
    match locationInfo.course_type:
        case CourseType.Pogo:
            return world.options.enable_pogo_stars.value == 1
        case CourseType.TinyToy:
            return world.options.enable_tiny_toy_stars.value == 1
        case CourseType.Jetpack:
            return world.options.enable_jetpack_stars.value == 1
        case CourseType.Chase:
            return world.options.enable_chase_the_grade_stars.value == 1
        case CourseType.AllCourseMarathon:
            return world.options.enable_all_course_stars.value == 1
        case _:
            match locationInfo.star_type:
                case StarType.MinTime:
                    return world.options.enable_time_stars.value == 1
                case StarType.NoDeaths:
                    return world.options.enable_no_deaths_stars.value == 1
                case StarType.GoldenPin | StarType.Comic:
                    return world.options.enable_collectible_stars.value == 1
                case StarType.Challenge:
                    return world.options.enable_challenge_stars.value == 1
                case StarType.Buddy:
                    return world.options.enable_buddy_stars.value == 1
                case StarType.BuddyChase:
                    return world.options.enable_buddy_chase_stars.value == 1
                case _:
                    return True

def evaluate_has_ability(state: CollectionState, ability: str, player: int):
    if (ability == "Special"):
        return state.has_any(["Double Jump", "Boost Jump", "Vault Jump"], player) or state.has_all(["Slide Jump", "Crouch"], player)
    elif(ability == "Slide Jump"):
        return state.has_all(["Slide Jump", "Crouch"], player)
    else:
        return state.has(ability, player)

def build_location(world: HotLavaWorld, region: Region, locationInfo: HotLavaLocationInfo) -> HotLavaLocation:
    location = HotLavaLocation(world.player, locationInfo.name, locationInfo.id, region)
    
    #TODO: allow the progress type to be configurable in options
    location.progress_type = get_location_progress_type(locationInfo)
        
    return location

def get_location_progress_type(locationInfo: HotLavaLocationInfo):
    match locationInfo.course_type:
        case CourseType.Pogo:
            return LocationProgressType.DEFAULT
        case CourseType.TinyToy:
            return LocationProgressType.DEFAULT
        case CourseType.Jetpack:
            return LocationProgressType.DEFAULT
        case CourseType.Chase:
            return LocationProgressType.DEFAULT
        case CourseType.AllCourseMarathon:
            return LocationProgressType.DEFAULT
        case _:
            match locationInfo.star_type:
                case StarType.CourseComplete | StarType.BuddyChase:
                    return LocationProgressType.DEFAULT
                case StarType.Buddy:
                    return LocationProgressType.DEFAULT
                case _:
                    return LocationProgressType.DEFAULT

def connect_regions(world: HotLavaWorld, source: str, target: str, rule: Optional[Callable[[CollectionState], bool]] = None) -> Entrance:
    sourceRegion = world.get_region(source)
    targetRegion = world.get_region(target)
    return sourceRegion.connect(targetRegion, rule=rule)