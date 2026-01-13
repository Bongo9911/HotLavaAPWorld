from BaseClasses import Location, LocationProgressType
from .Data import load_world_data
from .CourseType import CourseType


class HotLavaLocation(Location):
    game: str = "Hot Lava"

class HotLavaLocationInfo():
    id: int
    name: str
    progressType: LocationProgressType
    
    def __init__(self, id, name, progressType = LocationProgressType.DEFAULT):
        self.id = id
        self.name = name
        self.progressType = progressType

courses_by_world: dict[str, dict[str, list[HotLavaLocationInfo]]] = None

def build_locations_from_json():   
    worlds = load_world_data()

    courses_by_world = {}

    worldIdOffset = 100
    for world in worlds:
        course_table: dict[str, dict[str, HotLavaLocationInfo]] = {}
        courses_by_world[world["Name"]] = course_table

        courseIdOffset = 0
        for course in world["Courses"]:
            location_list: list[HotLavaLocationInfo] = []
            course_table[course["Name"]] = location_list
            
            for index, star in enumerate(course["Stars"]):
                progressType: LocationProgressType = LocationProgressType.DEFAULT
                if (course["CourseType"] == CourseType.Standard.value and index == 0):
                    progressType = LocationProgressType.PRIORITY
                elif ("Buddy" in star["Name"] or course["CourseType"] == CourseType.AllCourseMarathon.value):
                    progressType = LocationProgressType.EXCLUDED
                
                name: str = world["Name"] + " - " + course["Name"] + " - " + star["Name"]
                location: HotLavaLocationInfo = HotLavaLocationInfo(worldIdOffset + courseIdOffset + index, name, progressType)
                location_list.append(location)

            if (course["CourseType"] == CourseType.Standard.value):
                courseIdOffset += 10
            else:
                courseIdOffset += 1
        
        worldIdOffset += 100
    return courses_by_world

def get_courses_by_world():
    global courses_by_world
    
    if (courses_by_world == None):
        courses_by_world = build_locations_from_json()
    return courses_by_world

def get_location_name_to_id_for_all():
    courses_by_world = get_courses_by_world()
    
    loc_list: list[HotLavaLocationInfo] = []
    for world_name in courses_by_world:
        courses = courses_by_world[world_name]
        for d in courses:
            loc_list.extend(courses[d])
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