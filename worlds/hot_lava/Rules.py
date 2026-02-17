from __future__ import annotations

import random
from typing import Callable, Optional, TYPE_CHECKING, Union

from BaseClasses import CollectionState, MultiWorld
# from rule_builder.rules import CanReachLocation, Has, HasAny, Rule
from .CourseType import CourseType
from .Regions import connect_regions

from .StarType import StarType
from .Items import get_forcefield_name
from .Locations import get_all_location_infos, get_locations_info_for_world

from ..generic.Rules import set_rule

from .Options import HotLavaOptions, WorldSelect, get_enabled_world_names, option_id_to_world_name
from .Data import GameWorldInfo, game_world_dict

if TYPE_CHECKING:
    from .World import HotLavaWorld

def set_all_rules(world: HotLavaWorld):
    enabled_worlds: list[str] = get_enabled_world_names(world)
    
    unused_worlds = enabled_worlds.copy()
    first_world = option_id_to_world_name[world.options.start_world.value]
    last_world = option_id_to_world_name[world.options.last_world.value]
        
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
                    
    world_order = "Random"
    
    if world_order == "Random":
        random.shuffle(unused_worlds)
        
    if world.options.world_unlock_logic.value == world.options.world_unlock_logic.option_star_items:
        stars_per_world: dict[str, int] = {}
        
        stars_per_world[first_world] = 0
            
        star_factor = 10
        current_star_level = star_factor
            
        for world_name in unused_worlds:
            set_stars_for_world(world, world_name, current_star_level)
            stars_per_world[world_name] = current_star_level
            current_star_level += star_factor
        
        set_stars_for_world(world, last_world, current_star_level)
        stars_per_world[last_world] = current_star_level
        
    elif world.options.world_unlock_logic.value == world.options.world_unlock_logic.option_world_item:
        for world_name in enabled_worlds:
            set_rule(world.get_entrance(world_name + " Menu Item"),
                    lambda state, world_name=world_name: state.has("World Unlock - " + world_name, world.player))
    
    for world_name in enabled_worlds:
        game_world = game_world_dict[world_name]
        
        for connection in game_world.connections:
            source_region_name = world_name + " - " + connection.source_region
            target_region_name = world_name + " - " + connection.target_region
            
            rule: Optional[Callable[[CollectionState], bool]] = None
            #TODO waiting for rule builder to be built into exe client
            # rule: Optional[Union[Rule, Callable[[CollectionState], bool]]] = None
            
            if world.options.force_field_logic.value == world.options.force_field_logic.option_force_field_item:
                # rule = HasAny(*map(lambda forcefield: get_forcefield_name(world_name, forcefield), connection.force_fields))
                rule = lambda state, ff=connection.force_fields, wn=world_name: any(state.has(get_forcefield_name(wn, forcefield), world.player) for forcefield in ff)
            elif world.options.force_field_logic.value == world.options.force_field_logic.option_vanilla:
                # This logic is currently not able to be expressed with rule builder
                rule = lambda state, courses=connection.courses, gw=game_world: all(state.can_reach(get_complete_course_star_name(gw, course_name), "Location", world.player) for course_name in courses)
            
            connect_regions(world, source_region_name, target_region_name, rule=rule)    
    
    #TODO make this be a configurable option
    goal_type = "last_world_all_courses"
    
    if (goal_type == "last_world_all_courses"):
        victory_locations = [loc.name for loc in get_locations_info_for_world(last_world) 
            if loc.star_type == StarType.CourseComplete]
    else:
        victory_locations = [loc.name for loc in get_all_location_infos() 
            if loc.star_type == StarType.CourseComplete]
    
    world.multiworld.completion_condition[world.player] = lambda state: all(
        state.can_reach(world.get_location(loc), "Location", world.player) 
        for loc in victory_locations)
    
def set_stars_for_world(world: HotLavaWorld, world_name: str, star_level: int):
    set_rule(world.get_entrance(world_name + " Menu Item"),
                    lambda state, star_level=star_level: state.has("Star", world.player, star_level))
    
def get_complete_course_star_name(game_world: GameWorldInfo, course_name: str):
    course = next((course for course in game_world.courses if course.name == course_name), None)
    return game_world.name + " - " + course.name + " - " + course.stars[0].name