from __future__ import annotations

import math
import random
from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Item, ItemClassification
from .Options import get_enabled_world_names, option_id_to_world_name
from .Data import game_world_dict

if TYPE_CHECKING:
    from .World import HotLavaWorld

class HotLavaItem(Item):
    game: str = "Hot Lava"

class HotLavaItemData:
    code: int
    classification: ItemClassification = ItemClassification.progression
    
    def __init__(self, code, classification):
        self.code = code
        self.classification = classification
    
class HotLavaWorldUnlockItemData(HotLavaItemData):
    world_name: str
    
    def __init__(self, code, world_name, classification):
        super().__init__(code, classification)
        self.world_name = world_name
        
class HotLavaForceFieldItemData(HotLavaItemData):
    world_name: str
    
    def __init__(self, code, world_name, classification):
        super().__init__(code, classification)
        self.world_name = world_name

filler_items: dict[str, HotLavaItemData] = {
    "XP Shard": HotLavaItemData(1, ItemClassification.filler),
    "Star": HotLavaItemData(2, ItemClassification.progression_skip_balancing),
}

special_ability_items: dict[str, HotLavaItemData] = {
    "Double Jump": HotLavaItemData(10, ItemClassification.progression),
    "Boost Jump": HotLavaItemData(11, ItemClassification.progression),
    "Slide Jump": HotLavaItemData(12, ItemClassification.progression),
    "Vault Jump": HotLavaItemData(13, ItemClassification.progression),
}

standard_ability_items: dict[str, HotLavaItemData] = {
    "Crouch": HotLavaItemData(20, ItemClassification.progression),
    "Grab": HotLavaItemData(21, ItemClassification.progression),
    "Surf": HotLavaItemData(22, ItemClassification.progression),
    "Wall Jump": HotLavaItemData(23, ItemClassification.progression),
    "Swing": HotLavaItemData(24, ItemClassification.progression),
    "Climb": HotLavaItemData(25, ItemClassification.progression),
}

trial_items: dict[str, HotLavaItemData] = {
    "Pogo": HotLavaItemData(30, ItemClassification.progression),
    "Tiny Toy": HotLavaItemData(31, ItemClassification.progression),
    "Jetpack": HotLavaItemData(32, ItemClassification.progression),
}

character_items: dict[str, HotLavaItemData] = {
    # "Hazard": HotLavaItemData(40, ItemClassification.useful),
    "Jen Forcer": HotLavaItemData(41, ItemClassification.useful),
    "Lex Splorer": HotLavaItemData(42, ItemClassification.useful),
    "Sue Nami": HotLavaItemData(43, ItemClassification.useful),
    "Lord Sludge": HotLavaItemData(44, ItemClassification.useful),
    "Poizone": HotLavaItemData(45, ItemClassification.useful),
    "Infantry": HotLavaItemData(46, ItemClassification.useful),
    "Megamortabeast": HotLavaItemData(47, ItemClassification.useful),
    "Rambull": HotLavaItemData(48, ItemClassification.useful),
    "Stink Bomb": HotLavaItemData(49, ItemClassification.useful),
    "Venomess": HotLavaItemData(50, ItemClassification.useful),
    "Tyler Rex": HotLavaItemData(51, ItemClassification.useful),
    "Hera Scarlet": HotLavaItemData(52, ItemClassification.useful),
    "Leo": HotLavaItemData(53, ItemClassification.useful),
}

trap_items: dict[str, HotLavaItemData] = {
    "Slow Trap": HotLavaItemData(70, ItemClassification.trap),
}

head_accessories: dict[str, HotLavaItemData] = {
    "Bandana Hair": HotLavaItemData(2000, ItemClassification.filler),
    "'80s Hair": HotLavaItemData(2001, ItemClassification.filler),
    "The Natural": HotLavaItemData(2002, ItemClassification.filler),
    "Ancient Techno Helmet": HotLavaItemData(2003, ItemClassification.filler),
    "Angel Halo": HotLavaItemData(2004, ItemClassification.filler),
    "Swan Headpiece": HotLavaItemData(2005, ItemClassification.filler),
    "Balloon Glasses": HotLavaItemData(2006, ItemClassification.filler),
    "Shower Cap": HotLavaItemData(2007, ItemClassification.filler),
    "Beaksy": HotLavaItemData(2008, ItemClassification.filler),
    "Beret": HotLavaItemData(2009, ItemClassification.filler),
    "Bicycle Helmet": HotLavaItemData(2010, ItemClassification.filler),
    "Rad Hair": HotLavaItemData(2011, ItemClassification.filler),
    "Bow Hair Band": HotLavaItemData(2012, ItemClassification.filler),
    "Cardboard Knight Helm": HotLavaItemData(2013, ItemClassification.filler),
    "Buffalo Skull": HotLavaItemData(2014, ItemClassification.filler),
    "Bunny Ears and Nose": HotLavaItemData(2015, ItemClassification.filler),
    "Bunny Mask": HotLavaItemData(2016, ItemClassification.filler),
    "Calavera": HotLavaItemData(2017, ItemClassification.filler),
    "Cheerleader Hair": HotLavaItemData(2018, ItemClassification.filler),
    "Devil Ninja": HotLavaItemData(2019, ItemClassification.filler),
    "Dog Ears and Snout": HotLavaItemData(2020, ItemClassification.filler),
    "Dragon Horns": HotLavaItemData(2021, ItemClassification.filler),
    "Wilderness Troop Hat": HotLavaItemData(2022, ItemClassification.filler),
    "Don't Starve Knit Cap": HotLavaItemData(2023, ItemClassification.filler),
    "Eets": HotLavaItemData(2024, ItemClassification.filler),
    "Elf Hat": HotLavaItemData(2025, ItemClassification.filler),
    "Fez": HotLavaItemData(2026, ItemClassification.filler),
    "Fish Tank": HotLavaItemData(2027, ItemClassification.filler),
    "Flower Crown": HotLavaItemData(2028, ItemClassification.filler),
    "Kitsune Mask": HotLavaItemData(2029, ItemClassification.filler),
    "Grrr-illa Head": HotLavaItemData(2030, ItemClassification.filler),
    "Happy Little Hair": HotLavaItemData(2031, ItemClassification.filler),
    "Headphones": HotLavaItemData(2032, ItemClassification.filler),
    "Retro Headphones": HotLavaItemData(2033, ItemClassification.filler),
    "Holmes Hat": HotLavaItemData(2034, ItemClassification.filler),
    "Jester Hat": HotLavaItemData(2035, ItemClassification.filler),
    "King Wig": HotLavaItemData(2036, ItemClassification.filler),
    "Knight Helm": HotLavaItemData(2037, ItemClassification.filler),
    "Toque": HotLavaItemData(2038, ItemClassification.filler),
    "Leo's Helmet": HotLavaItemData(2039, ItemClassification.filler),
    "Kangaroo Mascot": HotLavaItemData(2040, ItemClassification.filler),
    "Mariachi Hat": HotLavaItemData(2041, ItemClassification.filler),
    "Bobby the Bobcat": HotLavaItemData(2042, ItemClassification.filler),
    "Turtle Mascot": HotLavaItemData(2043, ItemClassification.filler),
    "Mask": HotLavaItemData(2044, ItemClassification.filler),
    "Motobug Rider Head": HotLavaItemData(2045, ItemClassification.filler),
    "Nest": HotLavaItemData(2046, ItemClassification.filler),
    "Mark of the Ninja Head": HotLavaItemData(2047, ItemClassification.filler),
    "Octopus": HotLavaItemData(2048, ItemClassification.filler),
    "Party Hat": HotLavaItemData(2049, ItemClassification.filler),
    "Plague Mask": HotLavaItemData(2050, ItemClassification.filler),
    "Plumeria": HotLavaItemData(2051, ItemClassification.filler),
    "Yellow Polynesian": HotLavaItemData(2052, ItemClassification.filler),
    "Pink Polynesian": HotLavaItemData(2053, ItemClassification.filler),
    "My Pretty Pompadour": HotLavaItemData(2054, ItemClassification.filler),
    "Prospector Hat": HotLavaItemData(2055, ItemClassification.filler),
    "Jack-o'-lantern Head": HotLavaItemData(2056, ItemClassification.filler),
    "K.A.P.O.W! Helmet": HotLavaItemData(2057, ItemClassification.filler),
    "Helmet": HotLavaItemData(2058, ItemClassification.filler),
    "Road Crow Head": HotLavaItemData(2059, ItemClassification.filler),
    "Rockabilly Wig": HotLavaItemData(2060, ItemClassification.filler),
    "Samurai Helmet": HotLavaItemData(2061, ItemClassification.filler),
    "Hera's Helmet": HotLavaItemData(2062, ItemClassification.filler),
    '"Sheep..."': HotLavaItemData(2063, ItemClassification.filler),
    "Sombrero": HotLavaItemData(2064, ItemClassification.filler),
    "Swashbuckler Cap": HotLavaItemData(2065, ItemClassification.filler),
    "Thai-ger Face": HotLavaItemData(2066, ItemClassification.filler),
    "Turkey Hat": HotLavaItemData(2067, ItemClassification.filler),
    "Umbrella Hat": HotLavaItemData(2068, ItemClassification.filler),
    "Visor": HotLavaItemData(2069, ItemClassification.filler),
    "Virtual Reality Mask": HotLavaItemData(2070, ItemClassification.filler),
    "Don't Starve Wilson Mask": HotLavaItemData(2071, ItemClassification.filler),
    "Wizard Hat": HotLavaItemData(2072, ItemClassification.filler),
    "Wolf Ears and Snout": HotLavaItemData(2073, ItemClassification.filler),
    "Workout Hair": HotLavaItemData(2074, ItemClassification.filler),
    "Holiday Hat": HotLavaItemData(2075, ItemClassification.filler),
    "Bee Antennae": HotLavaItemData(2076, ItemClassification.filler),
    "Boater Hat": HotLavaItemData(2077, ItemClassification.filler),
    "Bonnet": HotLavaItemData(2078, ItemClassification.filler),
    "Bucket Hat": HotLavaItemData(2079, ItemClassification.filler),
    "Cat Ears": HotLavaItemData(2080, ItemClassification.filler),
    "Cowboy Hat": HotLavaItemData(2081, ItemClassification.filler),
    "Orange Daisy": HotLavaItemData(2082, ItemClassification.filler),
    "White Daisy": HotLavaItemData(2083, ItemClassification.filler),
    "Devil Horns": HotLavaItemData(2084, ItemClassification.filler),
    "Football Helmet": HotLavaItemData(2085, ItemClassification.filler),
    "Fur Hat": HotLavaItemData(2086, ItemClassification.filler),
    "Hard Hat": HotLavaItemData(2087, ItemClassification.filler),
    "Laser Knight Helmet": HotLavaItemData(2088, ItemClassification.filler),
    "Military Helmet": HotLavaItemData(2089, ItemClassification.filler),
    "Monocle": HotLavaItemData(2090, ItemClassification.filler),
    "Paper Hat": HotLavaItemData(2091, ItemClassification.filler),
    "Robin Hood Hat": HotLavaItemData(2092, ItemClassification.filler),
    "Skater Helmet": HotLavaItemData(2093, ItemClassification.filler),
    "Tinfoil Hat": HotLavaItemData(2094, ItemClassification.filler),
    "Top Hat": HotLavaItemData(2095, ItemClassification.filler),
    "Watch Cap": HotLavaItemData(2096, ItemClassification.filler),
    "Horned Helmet": HotLavaItemData(2097, ItemClassification.filler),
}

back_accessories: dict[str, HotLavaItemData] = {
    "Ancient Techno Armor": HotLavaItemData(2200, ItemClassification.filler),
    "Don't Starve Ancient Cane": HotLavaItemData(2201, ItemClassification.filler),
    "Angel Wings": HotLavaItemData(2202, ItemClassification.filler),
    "Hatchet": HotLavaItemData(2203, ItemClassification.filler),
    "Carving Axe": HotLavaItemData(2204, ItemClassification.filler),
    "Wrapped Hatchet": HotLavaItemData(2205, ItemClassification.filler),
    '"...Lollipop!"': HotLavaItemData(2206, ItemClassification.filler),
    "Open Backpack": HotLavaItemData(2207, ItemClassification.filler),
    "Balloon Sword & Armor": HotLavaItemData(2208, ItemClassification.filler),
    "Barbarian Armor": HotLavaItemData(2209, ItemClassification.filler),
    "Don't Starve Bee Fire Staff": HotLavaItemData(2210, ItemClassification.filler),
    "Don't Starve Bee Ice Staff": HotLavaItemData(2211, ItemClassification.filler),
    "Don't Starve Bee Spear": HotLavaItemData(2212, ItemClassification.filler),
    "Cardboard Knight Armor": HotLavaItemData(2213, ItemClassification.filler),
    "Bunny Body": HotLavaItemData(2214, ItemClassification.filler),
    "Don't Starve Walking Cane": HotLavaItemData(2215, ItemClassification.filler),
    "Cheerleader Top": HotLavaItemData(2216, ItemClassification.filler),
    "Crab Back Pack": HotLavaItemData(2217, ItemClassification.filler),
    "Bomb": HotLavaItemData(2218, ItemClassification.filler),
    "Dog Body": HotLavaItemData(2219, ItemClassification.filler),
    "Dragon Wings": HotLavaItemData(2220, ItemClassification.filler),
    "Don't Starve Umbrella": HotLavaItemData(2221, ItemClassification.filler),
    "Don't Starve Eye Bone": HotLavaItemData(2222, ItemClassification.filler),
    "Fork": HotLavaItemData(2223, ItemClassification.filler),
    "Grrr-illa Chest": HotLavaItemData(2224, ItemClassification.filler),
    "Don't Starve Ham Bat": HotLavaItemData(2225, ItemClassification.filler),
    "Happy Little Palette": HotLavaItemData(2226, ItemClassification.filler),
    "Jester Collar": HotLavaItemData(2227, ItemClassification.filler),
    "Jetpack (Accessory)": HotLavaItemData(2228, ItemClassification.filler),
    "Skeleton Key": HotLavaItemData(2229, ItemClassification.filler),
    "Royal Cape": HotLavaItemData(2230, ItemClassification.filler),
    "Klei Fest Shirt": HotLavaItemData(2231, ItemClassification.filler),
    "Lollipop": HotLavaItemData(2232, ItemClassification.filler),
    "Mango Creamsicle": HotLavaItemData(2233, ItemClassification.filler),
    "Motobug Armor": HotLavaItemData(2234, ItemClassification.filler),
    "Paint Roller": HotLavaItemData(2235, ItemClassification.filler),
    "Panda": HotLavaItemData(2236, ItemClassification.filler),
    "Plague Chest Armor": HotLavaItemData(2237, ItemClassification.filler),
    "Rainbow Lollipop": HotLavaItemData(2238, ItemClassification.filler),
    "Rainbow Popsicle": HotLavaItemData(2239, ItemClassification.filler),
    "Rainbow Wings": HotLavaItemData(2240, ItemClassification.filler),
    "Rambull's Vest": HotLavaItemData(2241, ItemClassification.filler),
    "K.A.P.O.W! Chest Plate": HotLavaItemData(2242, ItemClassification.filler),
    "Road Crow Chest": HotLavaItemData(2243, ItemClassification.filler),
    "Rockabilly Microphone": HotLavaItemData(2244, ItemClassification.filler),
    "Sai": HotLavaItemData(2245, ItemClassification.filler),
    "Scuba Gear": HotLavaItemData(2246, ItemClassification.filler),
    "Shovel": HotLavaItemData(2247, ItemClassification.filler),
    "Leaf Spear": HotLavaItemData(2248, ItemClassification.filler),
    "Crooked Spear": HotLavaItemData(2249, ItemClassification.filler),
    "Stinkbomb's Keytar": HotLavaItemData(2250, ItemClassification.filler),
    "Golden Hilted Sword": HotLavaItemData(2251, ItemClassification.filler),
    "Flying V Guitar": HotLavaItemData(2252, ItemClassification.filler),
    "Thai-ger Chest": HotLavaItemData(2253, ItemClassification.filler),
    "Powder Keg": HotLavaItemData(2254, ItemClassification.filler),
    "Sue's Ugly Xmas Sweater": HotLavaItemData(2255, ItemClassification.filler),
    "Tape Player": HotLavaItemData(2256, ItemClassification.filler),
    "Water Blaster": HotLavaItemData(2257, ItemClassification.filler),
    "Wizard Broom": HotLavaItemData(2258, ItemClassification.filler),
    "Wolf Body": HotLavaItemData(2259, ItemClassification.filler),
    "Workout Clothes": HotLavaItemData(2260, ItemClassification.filler),
    "Pugly Sweater": HotLavaItemData(2261, ItemClassification.filler),
    "Backpack": HotLavaItemData(2262, ItemClassification.filler),
    "Battle Axe": HotLavaItemData(2263, ItemClassification.filler),
    "Bazooka": HotLavaItemData(2264, ItemClassification.filler),
    "Bee Wings": HotLavaItemData(2265, ItemClassification.filler),
    "Boom Box": HotLavaItemData(2266, ItemClassification.filler),
    "Gold Boom Box": HotLavaItemData(2267, ItemClassification.filler),
    "Robin Hood Bow": HotLavaItemData(2268, ItemClassification.filler),
    "Cat Paw": HotLavaItemData(2269, ItemClassification.filler),
    "The Magenta Saber": HotLavaItemData(2270, ItemClassification.filler),
    "Devil Wings and Pitchfork": HotLavaItemData(2271, ItemClassification.filler),
    "Time Bomb": HotLavaItemData(2272, ItemClassification.filler),
    "Fairy Wings": HotLavaItemData(2273, ItemClassification.filler),
    "Football Jersey": HotLavaItemData(2274, ItemClassification.filler),
    "Acoustic Guitar": HotLavaItemData(2275, ItemClassification.filler),
    "Keytar": HotLavaItemData(2276, ItemClassification.filler),
    "Laser Knight Armour": HotLavaItemData(2277, ItemClassification.filler),
    "Glowing Sword and Shield": HotLavaItemData(2278, ItemClassification.filler),
    "Paper Sword": HotLavaItemData(2279, ItemClassification.filler),
    "Parachute Knapsack": HotLavaItemData(2280, ItemClassification.filler),
    "Torpedo": HotLavaItemData(2281, ItemClassification.filler),
    "Shark Fin": HotLavaItemData(2282, ItemClassification.filler),
    "Skateboard": HotLavaItemData(2283, ItemClassification.filler),
    "Surfboard": HotLavaItemData(2284, ItemClassification.filler),
    "Bear Backpack": HotLavaItemData(2285, ItemClassification.filler),
    "Viking Shield": HotLavaItemData(2286, ItemClassification.filler),
}

trinkets: dict[str, HotLavaItemData] = {
    "3D Glasses": HotLavaItemData(2400, ItemClassification.filler),
    "8-Bit Glasses": HotLavaItemData(2401, ItemClassification.filler),
    "Don't Starve's Abigail": HotLavaItemData(2402, ItemClassification.filler),
    "Ancient Techno Gloves": HotLavaItemData(2403, ItemClassification.filler),
    "Angel Wand": HotLavaItemData(2404, ItemClassification.filler),
    "Balloon Shoes": HotLavaItemData(2405, ItemClassification.filler),
    "Barbarian Gauntlets": HotLavaItemData(2406, ItemClassification.filler),
    "Bikini": HotLavaItemData(2407, ItemClassification.filler),
    "Black Beard": HotLavaItemData(2408, ItemClassification.filler),
    "Cardboard Knight Gauntlets": HotLavaItemData(2409, ItemClassification.filler),
    "Brainstorm's Glasses": HotLavaItemData(2410, ItemClassification.filler),
    "Brimstone Gilded Book": HotLavaItemData(2411, ItemClassification.filler),
    "Bunny Tail and Feet": HotLavaItemData(2412, ItemClassification.filler),
    "Cheerleader Dress": HotLavaItemData(2413, ItemClassification.filler),
    "The Chevron": HotLavaItemData(2414, ItemClassification.filler),
    "Dog Tail and Feet": HotLavaItemData(2415, ItemClassification.filler),
    "Gaming Gauntlet": HotLavaItemData(2416, ItemClassification.filler),
    "Dragon Tail": HotLavaItemData(2417, ItemClassification.filler),
    "Elf Ear": HotLavaItemData(2418, ItemClassification.filler),
    "Fox Tail": HotLavaItemData(2419, ItemClassification.filler),
    "Don't Starve's Goose/Moose": HotLavaItemData(2420, ItemClassification.filler),
    "Grrr-illa Feet": HotLavaItemData(2421, ItemClassification.filler),
    "Handlebar": HotLavaItemData(2422, ItemClassification.filler),
    "Heart Glasses": HotLavaItemData(2423, ItemClassification.filler),
    "Oxygen Not Included Dupe": HotLavaItemData(2424, ItemClassification.filler),
    "Don't Starve Wilson": HotLavaItemData(2425, ItemClassification.filler),
    "The Imperial": HotLavaItemData(2426, ItemClassification.filler),
    "Red Nose": HotLavaItemData(2427, ItemClassification.filler),
    "Clown Shoes": HotLavaItemData(2428, ItemClassification.filler),
    "King Scepter": HotLavaItemData(2429, ItemClassification.filler),
    "Maple Pin": HotLavaItemData(2430, ItemClassification.filler),
    "Mertail": HotLavaItemData(2431, ItemClassification.filler),
    "Motobug Belt": HotLavaItemData(2432, ItemClassification.filler),
    "Cockatiel": HotLavaItemData(2433, ItemClassification.filler),
    "Party Disguise Glasses": HotLavaItemData(2434, ItemClassification.filler),
    "Don't Starve Abigail Pin": HotLavaItemData(2435, ItemClassification.filler),
    "Don't Starve's Chester Pin": HotLavaItemData(2436, ItemClassification.filler),
    "Don't Starve's Wendy Pin": HotLavaItemData(2437, ItemClassification.filler),
    "Don't Starve's Willow Pin": HotLavaItemData(2438, ItemClassification.filler),
    "Don't Starve Wilson Pin": HotLavaItemData(2439, ItemClassification.filler),
    "Don't Starve's WX 78 Pin": HotLavaItemData(2440, ItemClassification.filler),
    "The Petite Handlebar": HotLavaItemData(2441, ItemClassification.filler),
    "Plague Gauntlets": HotLavaItemData(2442, ItemClassification.filler),
    "Prospecting Scarf and Beard": HotLavaItemData(2443, ItemClassification.filler),
    "Oxygen Not Included Puft": HotLavaItemData(2444, ItemClassification.filler),
    "Raccoon Tail": HotLavaItemData(2445, ItemClassification.filler),
    '"...Rainbow..."': HotLavaItemData(2446, ItemClassification.filler),
    "Rainbow Tail": HotLavaItemData(2447, ItemClassification.filler),
    "K.A.P.O.W! Leg Greaves": HotLavaItemData(2448, ItemClassification.filler),
    "Reading Glasses": HotLavaItemData(2449, ItemClassification.filler),
    "Red Beard": HotLavaItemData(2450, ItemClassification.filler),
    "Road Crow Arm Bands": HotLavaItemData(2451, ItemClassification.filler),
    "Rockabilly Glasses": HotLavaItemData(2452, ItemClassification.filler),
    "Sheriff Badge": HotLavaItemData(2453, ItemClassification.filler),
    "Trainers": HotLavaItemData(2454, ItemClassification.filler),
    "Basketball Shoes": HotLavaItemData(2455, ItemClassification.filler),
    "Workout Shoes": HotLavaItemData(2456, ItemClassification.filler),
    "Running Shoes": HotLavaItemData(2457, ItemClassification.filler),
    "Sloooooth": HotLavaItemData(2458, ItemClassification.filler),
    "Shutter Shades": HotLavaItemData(2459, ItemClassification.filler),
    "T.O.X.I.C.'s Lord Sludge": HotLavaItemData(2460, ItemClassification.filler),
    "Don't Starve Spider": HotLavaItemData(2461, ItemClassification.filler),
    "Star Glasses": HotLavaItemData(2462, ItemClassification.filler),
    "Squirrel Tail": HotLavaItemData(2463, ItemClassification.filler),
    "Thai-ger Feet and Tail": HotLavaItemData(2464, ItemClassification.filler),
    "Wizard Wand": HotLavaItemData(2465, ItemClassification.filler),
    "Wolf Feet and Tail": HotLavaItemData(2466, ItemClassification.filler),
    "Wolf Tail": HotLavaItemData(2467, ItemClassification.filler),
    "Workout Wristbands": HotLavaItemData(2468, ItemClassification.filler),
    "Seasonal Slippers": HotLavaItemData(2469, ItemClassification.filler),
    "Yellow Beard": HotLavaItemData(2470, ItemClassification.filler),
    "Bee Tail": HotLavaItemData(2471, ItemClassification.filler),
    "Boomerang": HotLavaItemData(2472, ItemClassification.filler),
    "Buddy": HotLavaItemData(2473, ItemClassification.filler),
    "Cat Tail": HotLavaItemData(2474, ItemClassification.filler),
    "Compass": HotLavaItemData(2475, ItemClassification.filler),
    "The Dali": HotLavaItemData(2476, ItemClassification.filler),
    "Devil Tail": HotLavaItemData(2477, ItemClassification.filler),
    "Dog Tail": HotLavaItemData(2478, ItemClassification.filler),
    "Shellholder": HotLavaItemData(2479, ItemClassification.filler),
    "Blue Laser Blade": HotLavaItemData(2480, ItemClassification.filler),
    "Nunchuck": HotLavaItemData(2481, ItemClassification.filler),
    "Powder Horn": HotLavaItemData(2482, ItemClassification.filler),
    "Robin Hood": HotLavaItemData(2483, ItemClassification.filler),
    "Rubber Duck": HotLavaItemData(2484, ItemClassification.filler),
    "Satchel": HotLavaItemData(2485, ItemClassification.filler),
    "4 Point Shuriken": HotLavaItemData(2486, ItemClassification.filler),
    "Forearm Spikes": HotLavaItemData(2487, ItemClassification.filler),
    "Wrist Sweatband": HotLavaItemData(2488, ItemClassification.filler),
    "Viking Axe": HotLavaItemData(2489, ItemClassification.filler),
    "Digital Watch": HotLavaItemData(2490, ItemClassification.filler),
}

accessory_items: dict[str, HotLavaItemData] = head_accessories | back_accessories | trinkets

decal_items: dict[str, HotLavaItemData] = {
    "Burger (Sticker)": HotLavaItemData(2600, ItemClassification.filler),
    "Cactus (Sticker)": HotLavaItemData(2601, ItemClassification.filler),
    "Can't Touch This (Sticker)": HotLavaItemData(2602, ItemClassification.filler),
    "Caution Hot Lava! (Sticker)": HotLavaItemData(2603, ItemClassification.filler),
    "Arrow (Sticker)": HotLavaItemData(2604, ItemClassification.filler),
    "Fresh (Sticker)": HotLavaItemData(2605, ItemClassification.filler),
    "Bonehead (Sticker)": HotLavaItemData(2606, ItemClassification.filler),
    "Hazardous Waste (Sticker)": HotLavaItemData(2607, ItemClassification.filler),
    "Franken Jen (Sticker)": HotLavaItemData(2608, ItemClassification.filler),
    "Lex Hex (Sticker)": HotLavaItemData(2609, ItemClassification.filler),
    "Deep Blue Sue (Sticker)": HotLavaItemData(2610, ItemClassification.filler),
    "Moccasin (Sticker)": HotLavaItemData(2611, ItemClassification.filler),
    "Rusty (Sticker)": HotLavaItemData(2612, ItemClassification.filler),
    "Slime Zero (Sticker)": HotLavaItemData(2613, ItemClassification.filler),
    "Ice Cream Cone (Sticker)": HotLavaItemData(2614, ItemClassification.filler),
    "Lightning Bolt (Sticker)": HotLavaItemData(2615, ItemClassification.filler),
    "Five out of Seven (Sticker)": HotLavaItemData(2616, ItemClassification.filler),
    "RNG Hands (Sticker)": HotLavaItemData(2617, ItemClassification.filler),
    "Skip (Sticker)": HotLavaItemData(2618, ItemClassification.filler),
    "Trebuchet (Sticker)": HotLavaItemData(2619, ItemClassification.filler),
    "Rainbow (Sticker)": HotLavaItemData(2620, ItemClassification.filler),
    "Rambull Logo (Sticker)": HotLavaItemData(2621, ItemClassification.filler),
    "Rest In Peace (Sticker)": HotLavaItemData(2622, ItemClassification.filler),
    "Bulldog Clip (Sticker)": HotLavaItemData(2623, ItemClassification.filler),
    "Calculator Watch (Sticker)": HotLavaItemData(2624, ItemClassification.filler),
    "Cellphone (Sticker)": HotLavaItemData(2625, ItemClassification.filler),
    "Portable Game (Sticker)": HotLavaItemData(2626, ItemClassification.filler),
    "White Glue (Sticker)": HotLavaItemData(2627, ItemClassification.filler),
    "Scissors (Sticker)": HotLavaItemData(2628, ItemClassification.filler),
    "Red Stapler (Sticker)": HotLavaItemData(2629, ItemClassification.filler),
    "Tack (Sticker)": HotLavaItemData(2630, ItemClassification.filler),
    "Smiley Face (Sticker)": HotLavaItemData(2631, ItemClassification.filler),
    "Watermelon (Sticker)": HotLavaItemData(2632, ItemClassification.filler),
    "You Must Be This Tall (Sticker)": HotLavaItemData(2633, ItemClassification.filler),
    "Hazard (Sticker)": HotLavaItemData(2634, ItemClassification.filler),
    "Jen Forcer (Sticker)": HotLavaItemData(2635, ItemClassification.filler),
    "Lex Splorer (Sticker)": HotLavaItemData(2636, ItemClassification.filler),
    "Poizone (Sticker)": HotLavaItemData(2637, ItemClassification.filler),
    "Sludge (Sticker)": HotLavaItemData(2638, ItemClassification.filler),
    "Sue Nami (Sticker)": HotLavaItemData(2639, ItemClassification.filler),
    "Happy Dolphin (Sticker)": HotLavaItemData(2640, ItemClassification.filler),
    "C.A.T. Hazard (Sticker)": HotLavaItemData(2641, ItemClassification.filler),
    "Rainbow Heart (Sticker)": HotLavaItemData(2642, ItemClassification.filler),
    "C.A.T. Jen Forcer (Sticker)": HotLavaItemData(2643, ItemClassification.filler),
    "C.A.T. Lex Splorer (Sticker)": HotLavaItemData(2644, ItemClassification.filler),
    "Pretty Pony (Sticker)": HotLavaItemData(2645, ItemClassification.filler),
    "Shelly (Sticker)": HotLavaItemData(2646, ItemClassification.filler),
    "C.A.T. Sue Nami (Sticker)": HotLavaItemData(2647, ItemClassification.filler),
    "Stink Bomb (Sticker)": HotLavaItemData(2648, ItemClassification.filler),
    "Tyler Rex (Sticker)": HotLavaItemData(2649, ItemClassification.filler),
    "Venomess (Sticker)": HotLavaItemData(2650, ItemClassification.filler),
    "On Point (Sticker)": HotLavaItemData(2651, ItemClassification.filler),
    "On Target (Sticker)": HotLavaItemData(2652, ItemClassification.filler),
    "Easy Mode (Sticker)": HotLavaItemData(2653, ItemClassification.filler),
    "Hazard, the Immortalixer Thrower (Sticker)": HotLavaItemData(2654, ItemClassification.filler),
    "Participation Ribbon (Sticker)": HotLavaItemData(2655, ItemClassification.filler),
    "Pogo Gang (Sticker)": HotLavaItemData(2656, ItemClassification.filler),
    "Salt (Sticker)": HotLavaItemData(2657, ItemClassification.filler),
    "Time Smash (Sticker)": HotLavaItemData(2658, ItemClassification.filler),
    "Pilot (Sticker)": HotLavaItemData(2659, ItemClassification.filler),
    "Full Cast Buddy (Sticker)": HotLavaItemData(2660, ItemClassification.filler),
    "Sore foot Buddy (Sticker)": HotLavaItemData(2661, ItemClassification.filler),
    "Injured Buddy (Sticker)": HotLavaItemData(2662, ItemClassification.filler),
    "Neck Brace Buddy (Sticker)": HotLavaItemData(2663, ItemClassification.filler),
    "Sore paw Buddy (Sticker)": HotLavaItemData(2664, ItemClassification.filler),
    "Sick Buddy (Sticker)": HotLavaItemData(2665, ItemClassification.filler),
    "Chef Buddy (Sticker)": HotLavaItemData(2666, ItemClassification.filler),
    "Budzo The Clown (Sticker)": HotLavaItemData(2667, ItemClassification.filler),
    "Diner Dog (Sticker)": HotLavaItemData(2668, ItemClassification.filler),
    "Pug, As You Are (Sticker)": HotLavaItemData(2669, ItemClassification.filler),
    "Pugman Hart (Sticker)": HotLavaItemData(2670, ItemClassification.filler),
    "Mountie Buddy (Sticker)": HotLavaItemData(2671, ItemClassification.filler),
    "Buddy Accountant (Sticker)": HotLavaItemData(2672, ItemClassification.filler),
    "Nurse Buddy (Sticker)": HotLavaItemData(2673, ItemClassification.filler),
    "Mr. Bud-T (Sticker)": HotLavaItemData(2674, ItemClassification.filler),
    "Poncho Pug (Sticker)": HotLavaItemData(2675, ItemClassification.filler),
    "Pugula (Sticker)": HotLavaItemData(2676, ItemClassification.filler),
    "Buddy Worker (Sticker)": HotLavaItemData(2677, ItemClassification.filler),
    "Anna Ka-roll-ina (Sticker)": HotLavaItemData(2678, ItemClassification.filler),
    "Brisco McBaggins (Sticker)": HotLavaItemData(2679, ItemClassification.filler),
    "MC Bronto (Sticker)": HotLavaItemData(2680, ItemClassification.filler),
    "Dylan Dimes (Sticker)": HotLavaItemData(2681, ItemClassification.filler),
    "DJ Spinosaurus (Sticker)": HotLavaItemData(2682, ItemClassification.filler),
    "Radical Dino Hazard (Sticker)": HotLavaItemData(2683, ItemClassification.filler),
    "Radical Dino Jen Forcer (Sticker)": HotLavaItemData(2684, ItemClassification.filler),
    "Radical Dino Lex Splorer (Sticker)": HotLavaItemData(2685, ItemClassification.filler),
    "Terry Dacta (Sticker)": HotLavaItemData(2686, ItemClassification.filler),
    "Jack the Sax Raptor (Sticker)": HotLavaItemData(2687, ItemClassification.filler),
    "Stevie Steg (Sticker)": HotLavaItemData(2688, ItemClassification.filler),
    "Radical Dino Sue Nami (Sticker)": HotLavaItemData(2689, ItemClassification.filler),
    "Rex Tyrano (Sticker)": HotLavaItemData(2690, ItemClassification.filler),
    "Tracey Tops (Sticker)": HotLavaItemData(2691, ItemClassification.filler),
    "Yoyo Joe (Sticker)": HotLavaItemData(2692, ItemClassification.filler),
    "Apple Scratch n' Sniff (Sticker)": HotLavaItemData(2693, ItemClassification.filler),
    "Artichoke Scratch n' Sniff (Sticker)": HotLavaItemData(2694, ItemClassification.filler),
    "Bacon Scratch n' Sniff (Sticker)": HotLavaItemData(2695, ItemClassification.filler),
    "Banana Scratch n' Sniff (Sticker)": HotLavaItemData(2696, ItemClassification.filler),
    "Broccoli Scratch n' Sniff (Sticker)": HotLavaItemData(2697, ItemClassification.filler),
    "Cherry Scratch n' Sniff (Sticker)": HotLavaItemData(2698, ItemClassification.filler),
    "Cottoncandy Scratch n' Sniff (Sticker)": HotLavaItemData(2699, ItemClassification.filler),
    "Cupcake Scratch n' Sniff (Sticker)": HotLavaItemData(2700, ItemClassification.filler),
    "Kiwi Scratch n' Sniff (Sticker)": HotLavaItemData(2701, ItemClassification.filler),
    "Lemon Scratch n' Sniff (Sticker)": HotLavaItemData(2702, ItemClassification.filler),
    "Peach Scratch n' Sniff (Sticker)": HotLavaItemData(2703, ItemClassification.filler),
    "Pear Scratch n' Sniff (Sticker)": HotLavaItemData(2704, ItemClassification.filler),
    "Pizza Scratch n' Sniff (Sticker)": HotLavaItemData(2705, ItemClassification.filler),
    "Plum Scratch n' Sniff (Sticker)": HotLavaItemData(2706, ItemClassification.filler),
    "Poop Scratch n' Sniff (Sticker)": HotLavaItemData(2707, ItemClassification.filler),
    "Popcorn Scratch n' Sniff (Sticker)": HotLavaItemData(2708, ItemClassification.filler),
    "Strawberry Scratch n' Sniff (Sticker)": HotLavaItemData(2709, ItemClassification.filler),
    "Teen Cyborca (Sticker)": HotLavaItemData(2710, ItemClassification.filler),
    "Teen Hazard (Sticker)": HotLavaItemData(2711, ItemClassification.filler),
    "Teen Jen (Sticker)": HotLavaItemData(2712, ItemClassification.filler),
    "Teen Lex (Sticker)": HotLavaItemData(2713, ItemClassification.filler),
    "Young Sludge (Sticker)": HotLavaItemData(2714, ItemClassification.filler),
    "Teen Sue (Sticker)": HotLavaItemData(2715, ItemClassification.filler),
}

world_unlock_items: dict[str, HotLavaWorldUnlockItemData] = None
# force_field_items: dict[str, HotLavaForceFieldItemData] = None

items_by_world: dict[str, dict[str, HotLavaItemData]] = None
item_data_table: dict[str, HotLavaItemData] = None

def build_items():
    global world_unlock_items
    world_unlock_items = {}
    # force_field_items = {}
    
    for world in game_world_dict.values():
        world_unlock_name = "World Unlock - " + world.name
        world_unlock_items[world_unlock_name] = HotLavaWorldUnlockItemData(world.item_id, world.name, ItemClassification.progression)
        
        # for force_field in world.force_fields:
        #     force_field_item_name = get_forcefield_name(world.name, force_field.name)
        #     force_field_items[force_field_item_name] = HotLavaForceFieldItemData(force_field.item_id, world.name, ItemClassification.progression)
            
def get_forcefield_name(world_name, forcefield_name):
    return world_name + " - Force Field Deactivate - " + forcefield_name

def get_all_items_table() -> dict[str, HotLavaItemData]:
    global item_data_table
    
    if (item_data_table == None):
        build_items()
        
        item_data_table = {**filler_items, **special_ability_items, **standard_ability_items, **trial_items, **character_items, **trap_items, **accessory_items, **decal_items, **world_unlock_items}
        
    return item_data_table

def create_all_items(world: HotLavaWorld):
    enabled_worlds: list[str] = get_enabled_world_names(world)
    
    total_items = 0
    
    # if (world.options.world_unlock_logic.value == world.options.world_unlock_logic.option_world_item):
    world_unlocks_to_add: list[str] = enabled_worlds.copy()
    # start_world_name: str = option_id_to_world_name[world.options.start_world.value]
    start_world_name: str = "Gym Class"
    
    # if(start_world_name == "Random"):
    #     start_world_name = random.choice(world_unlocks_to_add)
    # elif start_world_name not in world_unlocks_to_add:
    #     # TODO ERROR
    #     pass
    
    world_unlocks_to_add.remove(start_world_name)
    
    world.multiworld.push_precollected(world.create_item("World Unlock - " + start_world_name))
    
    for world_name in world_unlocks_to_add:
        item_name = next((key for key, value in world_unlock_items.items() if value.world_name == world_name), None)
        item = world.create_item(item_name)
        world.multiworld.itempool.append(item)
        total_items += 1
            
    # if (world.options.force_field_logic.value == world.options.force_field_logic.option_force_field_item):
    #     force_fields = [key for key, value in force_field_items.items() if value.world_name in enabled_worlds]
        
    #     for force_field_name in force_fields:
    #         item = world.create_item(force_field_name)
    #         world.multiworld.itempool.append(item)
    #         total_items += 1
            
    #TODO: Setting to enable/disable this
    total_items += create_items_from_dict(world, special_ability_items)
        
    #TODO: Setting to enable/disable this
    total_items += create_items_from_dict(world, standard_ability_items)
        
    enabled_trial_items = []
    
    if (world.options.enable_pogo_stars.value == 1):
        enabled_trial_items.append("Pogo")
    if (world.options.enable_tiny_toy_stars.value == 1):
        enabled_trial_items.append("Tiny Toy")
    if (world.options.enable_jetpack_stars.value == 1):
        enabled_trial_items.append("Jetpack")
        
    for trial_name in enabled_trial_items:
        item = world.create_item(trial_name)
        world.multiworld.itempool.append(item)
        total_items += 1
        
    total_items += create_items_from_dict(world, character_items)
            
    junk = world.get_total_locations() - total_items  # calculate this based on player options
    
    trap_item_count = math.ceil(junk * (world.options.trap_fill_percentage / 100))
    junk -= trap_item_count
    
    trap_item_names = list(trap_items.keys())
    
    while(trap_item_count > 0):
        trap_item_name = random.choice(trap_item_names)
        item = world.create_item(trap_item_name)
        world.multiworld.itempool.append(item)
        trap_item_count -= 1
    
    accessory_items_names = list(accessory_items.keys())
    
    while junk > 0 and len(accessory_items_names) > 0:
        accessory_item_name = random.choice(accessory_items_names)
        accessory_items_names.remove(accessory_item_name)
        item = world.create_item(accessory_item_name)
        world.multiworld.itempool.append(item)
        junk -= 1
        
    if(junk > 0):
        decal_items_names = list(decal_items.keys())
        
        while junk > 0 and len(decal_items_names) > 0:
            decal_item_name = random.choice(decal_items_names)
            decal_items_names.remove(decal_item_name)
            item = world.create_item(decal_item_name)
            world.multiworld.itempool.append(item)
            junk -= 1
    
    world.multiworld.itempool += [world.create_item("XP Shard") for _ in range(junk)]
    

def create_items_from_dict(world: HotLavaWorld, items: dict[str, HotLavaItemData]):
    for item_name in items:
        item = world.create_item(item_name)
        world.multiworld.itempool.append(item)
        
    return len(items)