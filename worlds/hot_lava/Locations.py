from BaseClasses import Location, LocationProgressType
from .Data import game_world_dict
from .CourseType import CourseType
from .StarType import StarType


class HotLavaLocation(Location):
    game: str = "Hot Lava"

class HotLavaLocationInfo():
    id: int
    name: str
    course_type: CourseType
    star_type: StarType
    required_abilities: list[list[str]] | None
    
    def __init__(self, id, name, course_type, star_type, required_abilities = None):
        self.id = id
        self.name = name
        self.course_type = course_type
        self.star_type = star_type
        self.required_abilities = required_abilities

courses_by_world: dict[str, dict[str, list[HotLavaLocationInfo]]] = None

additional_locations: list[HotLavaLocationInfo] = [
    HotLavaLocationInfo(1, "Intro - Complete the Intro.", CourseType.Standard, StarType.CourseComplete)
]

def build_locations():
    courses_by_world = {}

    for world in game_world_dict.values():
        course_table: dict[str, dict[str, HotLavaLocationInfo]] = {}
        courses_by_world[world.name] = course_table
        
        for course in world.courses:
            location_list: list[HotLavaLocationInfo] = []
            course_table[course.name] = location_list
            
            for star in course.stars:
                name: str = world.name + " - " + course.name + " - " + star.name
                if(star.required_abilities != None):
                    required_abilities = star.required_abilities
                else:
                    required_abilities = course.required_abilities
                location: HotLavaLocationInfo = HotLavaLocationInfo(star.id, name, course.course_type, star.star_type, required_abilities)
                location_list.append(location)
        
    return courses_by_world

def get_courses_by_world():
    global courses_by_world
    
    if (courses_by_world == None):
        courses_by_world = build_locations()
    return courses_by_world

def get_location_name_to_id_for_all():
    courses_by_world = get_courses_by_world()
    
    loc_list: list[HotLavaLocationInfo] = []
    for world_name in courses_by_world:
        courses = courses_by_world[world_name]
        for d in courses:
            loc_list.extend(courses[d])
            
    loc_list.extend(additional_locations)
            
    return { location.name: location.id for location in loc_list }

def get_location_name_to_id_for_world(world_name):
    courses = get_courses_by_world()[world_name]
    loc_list: list[HotLavaLocationInfo] = []
    for d in courses:
        loc_list.extend(courses[d])
    return { location.name: location.id for location in loc_list }

def get_location_name_to_id_for_course(world_name, course_name):
    return { location.name: location.id for location in get_courses_by_world()[world_name][course_name] }

def get_locations_info_for_course(world_name, course_name) -> list[HotLavaLocationInfo]:
    return get_courses_by_world()[world_name][course_name]

def get_locations_info_for_world(world_name) -> list[HotLavaLocationInfo]:
    courses = get_courses_by_world()[world_name]
    loc_list: list[HotLavaLocationInfo] = []
    for d in courses:
        loc_list.extend(courses[d])
    return loc_list

def get_all_location_infos() -> list[HotLavaLocationInfo]:
    worlds = get_courses_by_world()
    loc_list: list[HotLavaLocationInfo] = []
    for world in worlds:
        for course in worlds[world]:
            loc_list.extend(worlds[world][course])
    return loc_list