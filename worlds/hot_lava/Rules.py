import random
from typing import Callable, Optional, TYPE_CHECKING

from BaseClasses import CollectionState, MultiWorld
from .CourseType import CourseType
from .Regions import connect_regions, get_forcefield_name

from .StarType import StarType
from .Locations import get_all_location_infos, get_locations_info_for_world

from ..generic.Rules import set_rule

from .Options import HotLavaOptions
from .Data import GameWorldInfo, game_world_dict

if TYPE_CHECKING:
    from .World import HotLavaWorld

def set_rules(world: HotLavaWorld):
    enabled_worlds = ["Gym Class", "Playground", "School", "Wholesale", "Master Class", "Basement", "Rocco's Arcade"]
    unused_worlds = enabled_worlds.copy()
    first_world = "Gym Class"
    last_world = "Master Class"
    
    if first_world == "Random":
        first_world = random.choice(enabled_worlds)
        unused_worlds.remove(first_world)
    elif first_world in enabled_worlds:
        unused_worlds.remove(first_world)
    else:
        # TODO World was not in list of enabled worlds
        pass
        
    if last_world == "Random":
        last_world = random.choice(unused_worlds)
        unused_worlds.remove(last_world)
    elif last_world in unused_worlds:
        unused_worlds.remove(last_world)
    else:
        # TODO World was not in list of enabled worlds
        pass
                
    # self.stars_per_world[start_world] = 0
    
    world_order = "Random"
    
    if world_order == "Random":
        random.shuffle(unused_worlds)
        
    star_factor = 10
    current_star_level = star_factor
        
    for world_name in unused_worlds:
        set_stars_for_world(world, world_name, current_star_level)
        # self.stars_per_world[world_name] = current_star_level
        current_star_level += star_factor
    
    set_stars_for_world(world, last_world, current_star_level)
    # self.stars_per_world[end_world] = current_star_level
    
    # TODO make this be a configurable option
    force_field_logic = "vanilla"
    
    for world_name in enabled_worlds:
        game_world = game_world_dict[world_name]
        
        for connection in game_world.connections:
            source_region_name = world_name + " - " + connection.source_region
            target_region_name = world_name + " - " + connection.target_region
            
            rule: Optional[Callable[[CollectionState], bool]] = None
            
            if force_field_logic == "item":
                rule = lambda state, ff=connection.force_fields, wn=world_name: any(state.has(get_forcefield_name(wn, forcefield), world.player) for forcefield in ff)
            elif force_field_logic == "vanilla":
                rule = lambda state, courses=connection.courses, gw=game_world: all(state.can_reach(get_complete_course_star_name(gw, course_name), "Location", world.player) for course_name in courses)
            
            connect_regions(world, world.player, source_region_name, target_region_name, rule=rule)    
    
    #TODO make this be a configurable option
    goal_type = "last_world_all_courses"
    
    if (goal_type == "last_world_all_courses"):
        victory_locations = [loc.name for loc in get_locations_info_for_world(last_world) 
            if loc.starType == StarType.CourseComplete]
    else:
        victory_locations = [loc.name for loc in get_all_location_infos() 
            if loc.starType == StarType.CourseComplete]
    
    world.multiworld.completion_condition[world.player] = lambda state: all(
        state.can_reach(world.get_location(loc, world.player), "Location", world.player) 
        for loc in victory_locations)
    
def set_stars_for_world(world: HotLavaWorld, player: int, world_name: str, star_level: int):
    set_rule(world.get_entrance(world_name + " Menu Item", player),
                    lambda state, star_level=star_level: state.has("Star", player, star_level))
    
def get_complete_course_star_name(game_world: GameWorldInfo, course_name: str):
    course = next((course for course in game_world.courses if course.name == course_name), None)
    return game_world.name + " - " + course.name + " - " + course.stars[0].name