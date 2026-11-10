from __future__ import annotations

import random
from typing import Callable, Optional, TYPE_CHECKING, Union

from BaseClasses import CollectionState, MultiWorld
# from rule_builder.rules import CanReachLocation, Has, HasAny, Rule
from .CourseType import CourseType
from .Regions import connect_regions

from .StarType import StarType
from .Items import get_forcefield_name
from .Locations import HotLavaLocation, HotLavaLocationInfo, get_all_location_infos, get_locations_info_for_world, get_location_name_to_info

from ..generic.Rules import add_rule, set_rule

from .Options import HotLavaOptions, WorldSelect, get_enabled_world_names, option_id_to_world_name
from .Data import GameWorldInfo, game_world_dict

if TYPE_CHECKING:
    from .World import HotLavaWorld

# the full region name a Buddy/BuddyChase location's buddy AI must have walked over to reach it,
# or None if world_name has no Buddy/BuddyChase stars
def get_buddy_hub_region_name(world_name: str) -> str | None:
    buddy_hub_region = game_world_dict[world_name].buddy_hub_region
    if buddy_hub_region is None:
        return None
    return world_name + " - " + buddy_hub_region

def evaluate_has_ability(state: CollectionState, ability: str, player: int):
    if (ability == "Special"):
        return state.has_any(["Double Jump", "Boost Jump", "Vault Jump"], player) or state.has_all(["Slide Jump", "Crouch"], player)
    elif(ability == "Slide Jump"):
        return state.has_all(["Slide Jump", "Crouch"], player)
    else:
        return state.has(ability, player)

def set_location_access_rules(world: HotLavaWorld):
    location_infos = get_location_name_to_info()

    for location in world.multiworld.get_locations(world.player):
        if not isinstance(location, HotLavaLocation):
            continue

        location_info = location_infos.get(location.name)
        if location_info is None:
            continue

        if location_info.star_type == StarType.Buddy or location_info.star_type == StarType.BuddyChase:
            add_rule(location, lambda state: state.has("Grab", world.player))

            hub_region_name = get_buddy_hub_region_name(location_info.world_name)
            if hub_region_name is not None:
                # the buddy sub-region has exactly one entrance: the one created for it in Regions.py
                buddy_entrance = location.parent_region.entrances[0]
                add_rule(buddy_entrance, lambda state, hub=hub_region_name: state.can_reach_region(hub, world.player))

        if location_info.course_type == CourseType.Pogo:
            add_rule(location, lambda state: state.has("Pogo", world.player))
        elif location_info.course_type == CourseType.TinyToy:
            add_rule(location, lambda state: state.has("Tiny Toy", world.player))
        elif location_info.course_type == CourseType.Jetpack:
            add_rule(location, lambda state: state.has("Jetpack", world.player))

        required_abilities = location_info.required_abilities
        if required_abilities is not None:
            add_rule(location, lambda state, required_abilities=required_abilities: all(
                any(evaluate_has_ability(state, ability, world.player) for ability in or_group)
                for or_group in required_abilities
            ))

    set_rule(world.get_entrance("Rocco's Arcade - Arcade -> Rocco's Arcade - Arcade Rafters"),
                lambda state: state.has_all(["Climb", "Swing"], world.player))

def set_rules(world: HotLavaWorld):
    enabled_worlds: list[str] = get_enabled_world_names(world)
    
    # unused_worlds = enabled_worlds.copy()
    # first_world = option_id_to_world_name[world.options.start_world.value]
    # last_world = option_id_to_world_name[world.options.last_world.value]
        
    # if first_world == "Random":
    #     first_world = random.choice(enabled_worlds)
    #     unused_worlds.remove(first_world)
    # elif first_world in enabled_worlds:
    #     unused_worlds.remove(first_world)
    # else:
    #     # TODO World was not in list of enabled worlds
    #     pass
        
    # if last_world == "Random":
    #     last_world = random.choice(unused_worlds)
    #     unused_worlds.remove(last_world)
    # elif last_world in unused_worlds:
    #     unused_worlds.remove(last_world)
    # else:
    #     # TODO World was not in list of enabled worlds
    #     pass
                    
    # world_order = "Random"
    
    # if world_order == "Random":
    #     random.shuffle(unused_worlds)
        
    # if world.options.world_unlock_logic.value == world.options.world_unlock_logic.option_star_items:
    #     stars_per_world: dict[str, int] = {}
        
    #     stars_per_world[first_world] = 0
            
    #     star_factor = 10
    #     current_star_level = star_factor
            
    #     for world_name in unused_worlds:
    #         set_stars_for_world(world, world_name, current_star_level)
    #         stars_per_world[world_name] = current_star_level
    #         current_star_level += star_factor
        
    #     set_stars_for_world(world, last_world, current_star_level)
    #     stars_per_world[last_world] = current_star_level
        
    # elif world.options.world_unlock_logic.value == world.options.world_unlock_logic.option_world_item:
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
            
            # if world.options.force_field_logic.value == world.options.force_field_logic.option_force_field_item:
            #     # rule = HasAny(*map(lambda forcefield: get_forcefield_name(world_name, forcefield), connection.force_fields))
            #     rule = lambda state, ff=connection.force_fields, wn=world_name: any(state.has(get_forcefield_name(wn, forcefield), world.player) for forcefield in ff)
            # elif world.options.force_field_logic.value == world.options.force_field_logic.option_vanilla:
            #     # This logic is currently not able to be expressed with rule builder
            #     rule = lambda state, courses=connection.courses, gw=game_world: all(state.can_reach(get_complete_course_star_name(gw, course_name), "Location", world.player) for course_name in courses)
            
            connect_regions(world, source_region_name, target_region_name, rule=rule)    
    
    #TODO make this be a configurable option
    # goal_type = "last_world_all_courses"
    goal_type = "last_world_all_courses_trials"
    last_world = "Master Class"
    
    if (goal_type == "last_world_all_courses"):
        victory_locations = [loc.name for loc in get_locations_info_for_world(last_world) 
            if loc.star_type == StarType.CourseComplete]
    elif (goal_type == "last_world_all_courses_trials"):
        victory_locations = [loc.name for loc in get_locations_info_for_world(last_world) 
            if loc.star_type == StarType.CourseComplete or (loc.star_type == StarType.TrialComplete and loc.course_type != CourseType.AllCourseMarathon)]
    else:
        victory_locations = [loc.name for loc in get_all_location_infos() 
            if loc.star_type == StarType.CourseComplete]
    
    world.multiworld.completion_condition[world.player] = lambda state: all(
        state.can_reach(world.get_location(loc), "Location", world.player)
        for loc in victory_locations)

    set_location_access_rules(world)
    
def set_stars_for_world(world: HotLavaWorld, world_name: str, star_level: int):
    set_rule(world.get_entrance(world_name + " Menu Item"),
                    lambda state, star_level=star_level: state.has("Star", world.player, star_level))
    
def get_complete_course_star_name(game_world: GameWorldInfo, course_name: str):
    course = next((course for course in game_world.courses if course.name == course_name), None)
    return game_world.name + " - " + course.name + " - " + course.stars[0].name