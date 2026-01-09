import pkgutil
from typing import Any, Dict, List, Union
import orjson
from BaseClasses import Location


class HotLavaLocation(Location):
    game: str = "Hot Lava"


locations_by_world: dict = None

def load_json_data(data_name: str) -> Union[List[Any], Dict[str, Any]]:
    return orjson.loads(pkgutil.get_data(__name__, "data/" + data_name).decode("utf-8-sig"))

def build_locations_from_json():
    global locations_by_world
    
    worlds = load_json_data("game_worlds.json")

    locations_by_world = {}

    worldIdOffset = 100
    for world in worlds:
        location_table = {}
        locations_by_world[world["Name"]] = location_table

        courseIdOffset = 0
        for course in world["Courses"]:
            for index, star in enumerate(course["Stars"]):
                # TODO: These should be filtered out later so that IDs don't get messed up
                if (star["Name"] != "Buddy Mode"):
                    location_table[world["Name"] + " - " + course["Name"] + " - " + star["Name"]] = worldIdOffset + courseIdOffset + index
                    print(world["Name"] + " - " + course["Name"] + " - " + star["Name"])
                    print(worldIdOffset + courseIdOffset + index)

            if (course["CourseType"] == 0):
                courseIdOffset += 10
            else:
                courseIdOffset += 1
        
        worldIdOffset += 100
    return locations_by_world

def get_all_locations():
    global locations_by_world
    
    if (locations_by_world == None):
        locations_by_world = build_locations_from_json()
    return locations_by_world

def get_locations_for_world(world_name):
    return get_all_locations()[world_name]