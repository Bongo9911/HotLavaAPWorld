from dataclasses import dataclass, field

from .StarType import StarType
from .CourseType import CourseType

@dataclass
class GameStarInfo():
    id: int
    name: str
    star_type: StarType

@dataclass
class GameCourseInfo():
    name: str
    course_type: CourseType
    stars: list[GameStarInfo] = field(default_factory=list)

@dataclass
class GameWorldConnection():
    source_region: str
    target_region: str
    force_fields: list[str] = field(default_factory=list)
    # The list of courses needed to deactivate the force field in vanilla logic
    courses: list[str] = field(default_factory=list)
        
@dataclass
class GameForceFieldInfo():
    item_id: int
    name: str

@dataclass
class GameWorldInfo():
    item_id: int
    camel_case_name: str
    name: str
    courses: list[GameCourseInfo] = field(default_factory=list)
    connections: list[GameWorldConnection] = field(default_factory=list)
    force_fields: list[GameForceFieldInfo] = field(default_factory=list)
    
# Gym Class
gym_class = GameWorldInfo(
    100, "gym_class", "Gym Class",
    courses = [
        GameCourseInfo("Gym Jam", CourseType.Standard, [
            GameStarInfo(100, "Complete the course", StarType.CourseComplete),
            GameStarInfo(101, "Complete in under 08:00", StarType.MinTime),
            GameStarInfo(102, "Complete in under 02:10", StarType.MinTime),
            GameStarInfo(103, "Reach a speed of 9", StarType.Challenge),
            GameStarInfo(104, "No Deaths", StarType.NoDeaths),
            GameStarInfo(105, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(106, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Trampoline Trouble", CourseType.Standard, [
            GameStarInfo(110, "Complete the course", StarType.CourseComplete),
            GameStarInfo(111, "Complete in under 02:30", StarType.MinTime),
            GameStarInfo(112, "Complete in under 01:00", StarType.MinTime),
            GameStarInfo(113, "Don't perform any swings", StarType.Challenge),
            GameStarInfo(114, "No Deaths", StarType.NoDeaths),
            GameStarInfo(115, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(116, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Livin' on the Ledge", CourseType.Standard, [
            GameStarInfo(120, "Complete the course", StarType.CourseComplete),
            GameStarInfo(121, "Complete in under 02:00", StarType.MinTime),
            GameStarInfo(122, "Complete in under 00:55", StarType.MinTime),
            GameStarInfo(123, "Spend less than 25 seconds on the ground", StarType.Challenge),
            GameStarInfo(124, "No Deaths", StarType.NoDeaths),
            GameStarInfo(125, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(126, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Surfing Surfaces", CourseType.Standard, [
            GameStarInfo(130, "Complete the course", StarType.CourseComplete),
            GameStarInfo(131, "Complete in under 01:50", StarType.MinTime),
            GameStarInfo(132, "Complete in under 00:50", StarType.MinTime),
            GameStarInfo(133, "Reach a speed of 10.5", StarType.Challenge),
            GameStarInfo(134, "No Deaths", StarType.NoDeaths),
            GameStarInfo(135, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(136, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Pole Vault", CourseType.Standard, [
            GameStarInfo(140, "Complete the course", StarType.CourseComplete),
            GameStarInfo(141, "Complete in under 02:30", StarType.MinTime),
            GameStarInfo(142, "Complete in under 01:10", StarType.MinTime),
            GameStarInfo(143, "Spend less than 30 seconds on the ground", StarType.Challenge),
            GameStarInfo(144, "No Deaths", StarType.NoDeaths),
            GameStarInfo(145, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(146, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Chase Your Sister", CourseType.Standard, [
            GameStarInfo(150, "Complete the course", StarType.CourseComplete),
            GameStarInfo(151, "Complete in under 01:10", StarType.MinTime),
            GameStarInfo(152, "Complete in under 00:45", StarType.MinTime),
            GameStarInfo(153, "Don't perform any swings", StarType.Challenge),
            GameStarInfo(154, "Tag your sister", StarType.Challenge),
            GameStarInfo(155, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(156, "Wild Buddy Chase", StarType.BuddyChase),
        ]),
        GameCourseInfo("Pogo Trial", CourseType.Pogo, [
            GameStarInfo(160, "Find all the checkpoints using the Pogo Stick", StarType.TrialComplete),
        ]),
        GameCourseInfo("Tiny Toy Trial", CourseType.TinyToy, [
            GameStarInfo(161, "Get to the finish line", StarType.TrialComplete),
        ]),
        GameCourseInfo("Jetpack Trial", CourseType.Jetpack, [
            GameStarInfo(162, "Find all the checkpoints using the Jetpack", StarType.TrialComplete),
        ]),
        GameCourseInfo("All Course Marathon", CourseType.AllCourseMarathon, [
            GameStarInfo(163, "Complete the course", StarType.TrialComplete),
        ]),
    ],
    connections= [
        GameWorldConnection("Spawn", "Office Hallway", ["Gym/Office Hallway"], ["Trampoline Trouble"]),
        GameWorldConnection("Office Hallway", "Janitor's Closet", ["Office Hallway/Janitor's Closet"], ["Livin' on the Ledge"]),
        GameWorldConnection("Office Hallway", "Back Hallway", ["Office Hallway/Back Hallway"], ["Surfing Surfaces"]),
        GameWorldConnection("Spawn", "Back Hallway", ["Computer Lab Hallway/Back Hallway"], ["Surfing Surfaces"]),
        GameWorldConnection("Back Hallway", "Side Entrance", ["Back Hallway/Side Entrance"], ["Chase Your Sister"]),
    ],
    force_fields= [
        GameForceFieldInfo(110, "Gym/Office Hallway"),
        GameForceFieldInfo(111, "Office Hallway/Janitor's Closet"),
        GameForceFieldInfo(112, "Office Hallway/Back Hallway"),
        GameForceFieldInfo(113, "Computer Lab Hallway/Back Hallway"),
        GameForceFieldInfo(114, "Back Hallway/Side Entrance"),
    ]
)

# Playground
playground = GameWorldInfo(
    200, "playground", "Playground",
    [
        GameCourseInfo("Recess", CourseType.Standard, [
            GameStarInfo(200, "Complete the course", StarType.CourseComplete),
            GameStarInfo(201, "Complete in under 07:00", StarType.MinTime),
            GameStarInfo(202, "Complete in under 02:10", StarType.MinTime),
            GameStarInfo(203, "No Deaths", StarType.NoDeaths),
            GameStarInfo(204, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(205, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(206, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Big Kids Side", CourseType.Standard, [
            GameStarInfo(210, "Complete the course", StarType.CourseComplete),
            GameStarInfo(211, "Complete in under 08:00", StarType.MinTime),
            GameStarInfo(212, "Complete in under 02:45", StarType.MinTime),
            GameStarInfo(213, "No Deaths", StarType.NoDeaths),
            GameStarInfo(214, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(215, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(216, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Bouncy Castle", CourseType.Standard, [
            GameStarInfo(220, "Complete the course", StarType.CourseComplete),
            GameStarInfo(221, "Complete in under 04:30", StarType.MinTime),
            GameStarInfo(222, "Complete in under 01:45", StarType.MinTime),
            GameStarInfo(223, "No Deaths", StarType.NoDeaths),
            GameStarInfo(224, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(225, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(226, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Back to Class", CourseType.Standard, [
            GameStarInfo(230, "Complete the course", StarType.CourseComplete),
            GameStarInfo(231, "Complete in under 06:00", StarType.MinTime),
            GameStarInfo(232, "Complete in under 01:45", StarType.MinTime),
            GameStarInfo(233, "No Deaths", StarType.NoDeaths),
            GameStarInfo(234, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(235, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(236, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Sports Day", CourseType.Standard, [
            GameStarInfo(240, "Complete the course", StarType.CourseComplete),
            GameStarInfo(241, "Complete in under 01:40", StarType.MinTime),
            GameStarInfo(242, "Complete in under 01:10", StarType.MinTime),
            GameStarInfo(243, "No Deaths", StarType.NoDeaths),
            GameStarInfo(244, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(245, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(246, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Chase the Big Kid", CourseType.Standard, [
            GameStarInfo(250, "Complete the course", StarType.CourseComplete),
            GameStarInfo(251, "Complete in under 01:15", StarType.MinTime),
            GameStarInfo(252, "Complete in under 00:58", StarType.MinTime),
            GameStarInfo(253, "Tag your sister", StarType.Challenge),
            GameStarInfo(254, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(255, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(256, "Chase Buddy", StarType.BuddyChase),
        ]),
        GameCourseInfo("Pogo Trial 1", CourseType.Pogo, [
            GameStarInfo(260, "Find all the checkpoints using the Pogo Stick", StarType.TrialComplete),
        ]),
        GameCourseInfo("Pogo Trial 2", CourseType.Pogo, [
            GameStarInfo(261, "Find all the checkpoints using the Pogo Stick", StarType.TrialComplete),
        ]),
        GameCourseInfo("Tiny Toy Trial 1", CourseType.TinyToy, [
            GameStarInfo(262, "Get to the finish line", StarType.TrialComplete),
        ]),
        GameCourseInfo("Tiny Toy Trial 2", CourseType.TinyToy, [
            GameStarInfo(263, "Get to the finish line", StarType.TrialComplete),
        ]),
        GameCourseInfo("Jetpack Trial", CourseType.Jetpack, [
            GameStarInfo(264, "Find all the checkpoints using the Jetpack", StarType.TrialComplete),
        ]),
        GameCourseInfo("Chase the Grade", CourseType.Chase, [
            GameStarInfo(265, "Complete the course", StarType.TrialComplete),
        ]),
        GameCourseInfo("All Course Marathon", CourseType.AllCourseMarathon, [
            GameStarInfo(266, "Complete the course", StarType.TrialComplete),
        ]),
    ],
    connections= [
        GameWorldConnection("Spawn", "Basketball Courts", ["Spawn/Basketball Courts"], ["Recess"]),
        GameWorldConnection("Basketball Courts", "Sports Day Side", ["Basketball Courts/Sports Day Side"], ["Big Kids Side"]),
    ],
    force_fields= [
        GameForceFieldInfo(210, "Spawn/Basketball Courts"),
        GameForceFieldInfo(211, "Basketball Courts/Sports Day Side"),
    ]
)

# School
school = GameWorldInfo(
    300, "school", "School",
    [
        GameCourseInfo("ABCs and 123s", CourseType.Standard, [
            GameStarInfo(300, "Complete the course", StarType.CourseComplete),
            GameStarInfo(301, "Complete in under 12:00", StarType.MinTime),
            GameStarInfo(302, "Complete in under 05:00", StarType.MinTime),
            GameStarInfo(303, "No Deaths", StarType.NoDeaths),
            GameStarInfo(304, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(305, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(306, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Middle School Mischief", CourseType.Standard, [
            GameStarInfo(310, "Complete the course", StarType.CourseComplete),
            GameStarInfo(311, "Complete in under 11:00", StarType.MinTime),
            GameStarInfo(312, "Complete in under 03:00", StarType.MinTime),
            GameStarInfo(313, "No Deaths", StarType.NoDeaths),
            GameStarInfo(314, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(315, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(316, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Repeat the Grade", CourseType.Standard, [
            GameStarInfo(320, "Complete the course", StarType.CourseComplete),
            GameStarInfo(321, "Complete in under 10:00", StarType.MinTime),
            GameStarInfo(322, "Complete in under 03:30", StarType.MinTime),
            GameStarInfo(323, "No Deaths", StarType.NoDeaths),
            GameStarInfo(324, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(325, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(326, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Senior Trip", CourseType.Standard, [
            GameStarInfo(330, "Complete the course", StarType.CourseComplete),
            GameStarInfo(331, "Complete in under 08:00", StarType.MinTime),
            GameStarInfo(332, "Complete in under 03:00", StarType.MinTime),
            GameStarInfo(333, "No Deaths", StarType.NoDeaths),
            GameStarInfo(334, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(335, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(336, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Freshman Frenzy", CourseType.Standard, [
            GameStarInfo(340, "Complete the course", StarType.CourseComplete),
            GameStarInfo(341, "Complete in under 10:00", StarType.MinTime),
            GameStarInfo(342, "Complete in under 03:30", StarType.MinTime),
            GameStarInfo(343, "No Deaths", StarType.NoDeaths),
            GameStarInfo(344, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(345, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(346, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Chase Your Sister", CourseType.Standard, [
            GameStarInfo(350, "Complete the course", StarType.CourseComplete),
            GameStarInfo(351, "Complete in under 02:00", StarType.MinTime),
            GameStarInfo(352, "Complete in under 00:50", StarType.MinTime),
            GameStarInfo(353, "Tag your sister", StarType.Challenge),
            GameStarInfo(354, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(355, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(356, "Chase The Escaped Dog", StarType.BuddyChase),
        ]),
        GameCourseInfo("Pogo Trial 1", CourseType.Pogo, [
            GameStarInfo(360, "Find all the checkpoints using the Pogo Stick", StarType.TrialComplete),
        ]),
        GameCourseInfo("Pogo Trial 2", CourseType.Pogo, [
            GameStarInfo(361, "Find all the checkpoints using the Pogo Stick", StarType.TrialComplete),
        ]),
        GameCourseInfo("Pogo Trial 3", CourseType.Pogo, [
            GameStarInfo(362, "Find all the checkpoints using the Pogo Stick", StarType.TrialComplete),
        ]),
        GameCourseInfo("Tiny Toy Trial", CourseType.TinyToy, [
            GameStarInfo(363, "Get to the finish line", StarType.TrialComplete),
        ]),
        GameCourseInfo("Jetpack Trial", CourseType.Jetpack, [
            GameStarInfo(364, "Find all the checkpoints using the Jetpack", StarType.TrialComplete),
        ]),
        GameCourseInfo("Chase the Grade", CourseType.Chase, [
            GameStarInfo(365, "Complete the course", StarType.TrialComplete),
        ]),
        GameCourseInfo("All Course Marathon", CourseType.AllCourseMarathon, [
            GameStarInfo(366, "Complete the course", StarType.TrialComplete),
        ]),
    ],
    connections= [
        GameWorldConnection("Atrium", "Teacher's Lounge", ["English Hallway/Teacher's Lounge Hallway"], ["ABCs and 123s"]),
        GameWorldConnection("Teacher's Lounge", "Courtyard", ["Teacher's Lounge/Courtyard"], ["ABCs and 123s", "Middle School Mischief", "Repeat the Grade"]),
        GameWorldConnection("Teacher's Lounge", "Art Hallway", ["Teacher's Lounge Hallway/Art Hallway"], ["ABCs and 123s", "Middle School Mischief"]),
        GameWorldConnection("Art Hallway", "Gym Hallway"),
        GameWorldConnection("Gym Hallway", "Gym"),
        GameWorldConnection("Atrium", "Cafeteria", [], ["ABCs and 123s", "Middle School Mischief"]), #TODO: add back force field names
        GameWorldConnection("Cafeteria", "Social Studies Hallway"),
        GameWorldConnection("Atrium", "Social Studies Hallway", [], ["ABCs and 123s", "Middle School Mischief"]), #TODO: add back force field names
        GameWorldConnection("Social Studies Hallway", "Social Studies Class", [], ["Pogo Trial 1", "Pogo Trial 2"]), #TODO: add back force field names
        GameWorldConnection("Social Studies Hallway", "Art Hallway", ["Social Studies Hallway/Art Hallway"], ["ABCs and 123s", "Middle School Mischief"]),
        GameWorldConnection("Art Hallway", "Art Class", ["Art Hallway/Art Class"], ["Chase Your Sister"]),
        GameWorldConnection("Art Class", "Art Closet", ["Art Closet/Art Class"], ["Chase Your Sister"]),
        GameWorldConnection("Gym Hallway", "Science Lab", [], ["ABCs and 123s", "Middle School Mischief", "Repeat the Grade", "Senior Trip", "Freshman Frenzy"]), #TODO: add back force field names
        GameWorldConnection("Science Lab", "Art Closet", ["Science Lab/Art Closet"], ["ABCs and 123s", "Middle School Mischief", "Repeat the Grade", "Senior Trip", "Freshman Frenzy"]),
        GameWorldConnection("Gym Hallway", "Computer Lab", ["Gym Hallway/Computer Lab"], ["ABCs and 123s", "Middle School Mischief", "Repeat the Grade", "Senior Trip"]),
    ],
    force_fields= [
        GameForceFieldInfo(310, "Gym Hallway/Computer Lab"),
        GameForceFieldInfo(311, "Social Studies Hallway/Art Hallway"),
        GameForceFieldInfo(312, "Teacher's Lounge Hallway/Art Hallway"),
        GameForceFieldInfo(313, "English Hallway/Teacher's Lounge Hallway"),
        GameForceFieldInfo(314, "Science Lab/Art Closet"),
        GameForceFieldInfo(315, "Art Hallway/Art Class"),
        GameForceFieldInfo(316, "Art Closet/Art Class"),
        GameForceFieldInfo(317, "Teacher's Lounge/Courtyard"),
    ]
)

# Wholesale
wholesale = GameWorldInfo(
    400, "wholesale", "Wholesale",
    [
        GameCourseInfo("To the Top", CourseType.Standard, [
            GameStarInfo(400, "Complete the course", StarType.CourseComplete),
            GameStarInfo(401, "Complete in under 10:00", StarType.MinTime),
            GameStarInfo(402, "Complete in under 03:00", StarType.MinTime),
            GameStarInfo(403, "No Deaths", StarType.NoDeaths),
            GameStarInfo(404, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(405, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(406, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Duct and Cover", CourseType.Standard, [
            GameStarInfo(410, "Complete the course", StarType.CourseComplete),
            GameStarInfo(411, "Complete in under 08:00", StarType.MinTime),
            GameStarInfo(412, "Complete in under 02:30", StarType.MinTime),
            GameStarInfo(413, "No Deaths", StarType.NoDeaths),
            GameStarInfo(414, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(415, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(416, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Meat Market", CourseType.Standard, [
            GameStarInfo(420, "Complete the course", StarType.CourseComplete),
            GameStarInfo(421, "Complete in under 08:00", StarType.MinTime),
            GameStarInfo(422, "Complete in under 03:30", StarType.MinTime),
            GameStarInfo(423, "No Deaths", StarType.NoDeaths),
            GameStarInfo(424, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(425, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(426, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Returns", CourseType.Standard, [
            GameStarInfo(430, "Complete the course", StarType.CourseComplete),
            GameStarInfo(431, "Complete in under 04:00", StarType.MinTime),
            GameStarInfo(432, "Complete in under 02:30", StarType.MinTime),
            GameStarInfo(433, "No Deaths", StarType.NoDeaths),
            GameStarInfo(434, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(435, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(436, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Meat Grinder", CourseType.Standard, [
            GameStarInfo(440, "Complete the course", StarType.CourseComplete),
            GameStarInfo(441, "Complete in under 10:00", StarType.MinTime),
            GameStarInfo(442, "Complete in under 04:30", StarType.MinTime),
            GameStarInfo(443, "No Deaths", StarType.NoDeaths),
            GameStarInfo(444, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(445, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(446, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Chase Through the Store", CourseType.Standard, [
            GameStarInfo(450, "Complete the course", StarType.CourseComplete),
            GameStarInfo(451, "Complete in under 00:50", StarType.MinTime),
            GameStarInfo(452, "Complete in under 00:33", StarType.MinTime),
            GameStarInfo(453, "No Deaths", StarType.NoDeaths),
            GameStarInfo(454, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(455, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(456, "Chase the Runaway Dog", StarType.BuddyChase),
        ]),
        GameCourseInfo("Pogo Trial 1", CourseType.Pogo, [
            GameStarInfo(460, "Find all the checkpoints using the Pogo Stick", StarType.TrialComplete),
        ]),
        GameCourseInfo("Pogo Trial 2", CourseType.Pogo, [
            GameStarInfo(461, "Find all the checkpoints using the Pogo Stick", StarType.TrialComplete),
        ]),
        GameCourseInfo("Pogo Trial 3", CourseType.Pogo, [
            GameStarInfo(462, "Find all the checkpoints using the Pogo Stick", StarType.TrialComplete),
        ]),
        GameCourseInfo("Tiny Toy Trial", CourseType.TinyToy, [
            GameStarInfo(463, "Get to the finish line", StarType.TrialComplete),
        ]),
        GameCourseInfo("Jetpack Trial", CourseType.Jetpack, [
            GameStarInfo(464, "Find all the checkpoints using the Jetpack", StarType.TrialComplete),
        ]),
        GameCourseInfo("Chase the Grade", CourseType.Chase, [
            GameStarInfo(465, "Complete the course", StarType.TrialComplete),
        ]),
        GameCourseInfo("All Course Marathon", CourseType.AllCourseMarathon, [
            GameStarInfo(466, "Complete the course", StarType.TrialComplete),
        ]),
    ],
    connections= [
        GameWorldConnection("Employee Hallway", "Breakroom", ["Employee Hallway/Breakroom"], ["To the Top", "Duct and Cover", "Meat Market"]),
        GameWorldConnection("Employee Hallway", "Janitor's Closet", ["Employee Hallway/Janitor's Closet"], ["Pogo Trial 1", "Pogo Trial 2"]),
        GameWorldConnection("Employee Hallway", "Checkout", ["Employee Hallway/Checkout"], ["To the Top"]),
        GameWorldConnection("Checkout", "Cart Storage", ["Checkout/Cart Storage"], ["Pogo Trial 1"]),
        GameWorldConnection("Checkout", "Shopping Area", ["Checkout/Shopping Area"], ["To the Top", "Duct and Cover"]),
        GameWorldConnection("Shopping Area", "Under the Shelves", ["Under the Shelves"], ["To the Top", "Duct and Cover", "Meat Market", "Returns", "Meat Grinder", "Chase Through the Store"]),
    ],
    force_fields= [
        GameForceFieldInfo(410, "Employee Hallway/Checkout"),
        GameForceFieldInfo(411, "Employee Hallway/Janitor's Closet"),
        GameForceFieldInfo(412, "Under the Shelves"),
        GameForceFieldInfo(413, "Checkout/Cart Storage"),
        GameForceFieldInfo(414, "Employee Hallway/Breakroom"),
        GameForceFieldInfo(415, "Checkout/Shopping Area"),
    ]
)

# Master Class
master_class = GameWorldInfo(
    500, "master_class", "Master Class",
    [
        GameCourseInfo("Air Control Mastery", CourseType.Standard, [
            GameStarInfo(500, "Complete the course", StarType.CourseComplete),
            GameStarInfo(501, "Complete in under 02:30", StarType.MinTime),
            GameStarInfo(502, "Complete in under 01:00", StarType.MinTime),
            GameStarInfo(503, "No Deaths", StarType.NoDeaths),
            GameStarInfo(504, "Reach a speed of 4.5", StarType.Challenge),
            GameStarInfo(505, "Grab the golden pin", StarType.GoldenPin),
        ]),
        GameCourseInfo("Wall Jump Mastery", CourseType.Standard, [
            GameStarInfo(510, "Complete the course", StarType.CourseComplete),
            GameStarInfo(511, "Complete in under 02:30", StarType.MinTime),
            GameStarInfo(512, "Complete in under 00:50", StarType.MinTime),
            GameStarInfo(513, "No Deaths", StarType.NoDeaths),
            GameStarInfo(514, "Spend less than 10 seconds on the ground", StarType.Challenge),
            GameStarInfo(515, "Grab the golden pin", StarType.GoldenPin),
        ]),
        GameCourseInfo("Surf Mastery", CourseType.Standard, [
            GameStarInfo(520, "Complete the course", StarType.CourseComplete),
            GameStarInfo(521, "Complete in under 01:00", StarType.MinTime),
            GameStarInfo(522, "Complete in under 00:30", StarType.MinTime),
            GameStarInfo(523, "No Deaths", StarType.NoDeaths),
            GameStarInfo(524, "Complete in 5 jumps or less", StarType.Challenge),
            GameStarInfo(525, "Grab the golden pin", StarType.GoldenPin),
        ]),
        GameCourseInfo("Boosting Mastery", CourseType.Standard, [
            GameStarInfo(530, "Complete the course", StarType.CourseComplete),
            GameStarInfo(531, "Complete in under 04:00", StarType.MinTime),
            GameStarInfo(532, "Complete in under 01:00", StarType.MinTime),
            GameStarInfo(533, "No Deaths", StarType.NoDeaths),
            GameStarInfo(534, "Reach a speed of 5.5", StarType.Challenge),
            GameStarInfo(535, "Grab the golden pin", StarType.GoldenPin),
        ]),
        GameCourseInfo("Wind Tunnel Mastery", CourseType.Standard, [
            GameStarInfo(540, "Complete the course", StarType.CourseComplete),
            GameStarInfo(541, "Complete in under 01:00", StarType.MinTime),
            GameStarInfo(542, "Complete in under 00:30", StarType.MinTime),
            GameStarInfo(543, "No Deaths", StarType.NoDeaths),
            GameStarInfo(544, "Spend less than 5 seconds on the ground", StarType.Challenge),
            GameStarInfo(545, "Grab the golden pin", StarType.GoldenPin),
        ]),
        GameCourseInfo("Honors Gym Class", CourseType.Standard, [
            GameStarInfo(550, "Complete the course", StarType.CourseComplete),
            GameStarInfo(551, "Complete in under 04:30", StarType.MinTime),
            GameStarInfo(552, "Complete in under 02:00", StarType.MinTime),
            GameStarInfo(553, "No Deaths", StarType.NoDeaths),
            GameStarInfo(554, "Reach a speed of 9", StarType.Challenge),
            GameStarInfo(555, "Grab the golden pin", StarType.GoldenPin),
        ]),
        GameCourseInfo("Pogo Trial", CourseType.Pogo, [
            GameStarInfo(560, "Find all the checkpoints using the Pogo Stick", StarType.TrialComplete),
        ]),
        GameCourseInfo("Tiny Toy Trial", CourseType.TinyToy, [
            GameStarInfo(561, "Get to the finish line", StarType.TrialComplete),
        ]),
        GameCourseInfo("Jetpack Trial", CourseType.Jetpack, [
            GameStarInfo(562, "Find all the checkpoints using the Jetpack", StarType.TrialComplete),
        ]),
        GameCourseInfo("All Course Marathon", CourseType.AllCourseMarathon, [
            GameStarInfo(563, "Complete the course", StarType.TrialComplete),
        ]),
    ]
)

# Basement
basement = GameWorldInfo(
    600, "basement", "Basement",
    [
        GameCourseInfo("Race to the Summit", CourseType.Standard, [
            GameStarInfo(600, "Complete the course", StarType.CourseComplete),
            GameStarInfo(601, "Complete in under 05:00", StarType.MinTime),
            GameStarInfo(602, "Complete in under 02:00", StarType.MinTime),
            GameStarInfo(603, "No Deaths", StarType.NoDeaths),
            GameStarInfo(604, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(605, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(606, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Lights Out", CourseType.Standard, [
            GameStarInfo(610, "Complete the course", StarType.CourseComplete),
            GameStarInfo(611, "Complete in under 03:00", StarType.MinTime),
            GameStarInfo(612, "Complete in under 00:45", StarType.MinTime),
            GameStarInfo(613, "No Deaths", StarType.NoDeaths),
            GameStarInfo(614, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(615, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(616, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Temple Sprint", CourseType.Standard, [
            GameStarInfo(620, "Complete the course", StarType.CourseComplete),
            GameStarInfo(621, "Complete in under 04:20", StarType.MinTime),
            GameStarInfo(622, "Complete in under 01:30", StarType.MinTime),
            GameStarInfo(623, "No Deaths", StarType.NoDeaths),
            GameStarInfo(624, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(625, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(626, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Fancy Footwork", CourseType.Standard, [
            GameStarInfo(630, "Complete the course", StarType.CourseComplete),
            GameStarInfo(631, "Complete in under 06:00", StarType.MinTime),
            GameStarInfo(632, "Complete in under 02:00", StarType.MinTime),
            GameStarInfo(633, "No Deaths", StarType.NoDeaths),
            GameStarInfo(634, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(635, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(636, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Minecart Carnage", CourseType.Standard, [
            GameStarInfo(640, "Complete the course", StarType.CourseComplete),
            GameStarInfo(641, "Complete in under 08:00", StarType.MinTime),
            GameStarInfo(642, "Complete in under 02:45", StarType.MinTime),
            GameStarInfo(643, "No Deaths", StarType.NoDeaths),
            GameStarInfo(644, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(645, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(646, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Chase The Meaning", CourseType.Standard, [
            GameStarInfo(650, "Complete the course", StarType.CourseComplete),
            GameStarInfo(651, "Complete in under 03:00", StarType.MinTime),
            GameStarInfo(652, "Complete in under 01:30", StarType.MinTime),
            GameStarInfo(653, "Tag your sister", StarType.Challenge),
            GameStarInfo(654, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(655, "Find the hidden G.A.T. comic", StarType.Comic),
            GameStarInfo(656, "Wild Teddy Chase", StarType.BuddyChase),
        ]),
        GameCourseInfo("Pogo Trial", CourseType.Pogo, [
            GameStarInfo(660, "Find all the checkpoints using the Pogo Stick", StarType.TrialComplete),
        ]),
        GameCourseInfo("Tiny Toy Trial", CourseType.TinyToy, [
            GameStarInfo(661, "Get to the finish line", StarType.TrialComplete),
        ]),
        GameCourseInfo("Jetpack Trial", CourseType.Jetpack, [
            GameStarInfo(662, "Find all the checkpoints using the Jetpack", StarType.TrialComplete),
        ]),
        GameCourseInfo("All Course Marathon", CourseType.AllCourseMarathon, [
            GameStarInfo(663, "Complete the course", StarType.TrialComplete),
        ]),
    ],
    connections= [
        GameWorldConnection("Foyer", "Living Room", ["Foyer/Living Room"], ["Lights Out"]),
        GameWorldConnection("Foyer", "Dining Room", ["Foyer/Dining Room"], ["Temple Sprint"]),
        GameWorldConnection("Dining Room", "Kitchen"),
        GameWorldConnection("Kitchen", "Basement Storage", ["Kitchen/Basement Storage"], ["Fancy Footwork"]),
        GameWorldConnection("Basement Storage", "Den", ["Basement Storage/Den"], ["Chase The Meaning"]),
    ],
    force_fields= [
        GameForceFieldInfo(610, "Foyer/Living Room"),
        GameForceFieldInfo(611, "Foyer/Dining Room"),
        GameForceFieldInfo(612, "Kitchen/Basement Storage"),
        GameForceFieldInfo(613, "Basement Storage/Den"),
    ]
)

# Rocco's Arcade
roccos_arcade = GameWorldInfo(
    700, "roccos_arcade", "Rocco's Arcade",
    [
        GameCourseInfo("Arcade Action", CourseType.Standard, [
            GameStarInfo(700, "Complete the course", StarType.CourseComplete),
            GameStarInfo(701, "Complete in under 02:50", StarType.MinTime),
            GameStarInfo(702, "Complete in under 01:15", StarType.MinTime),
            GameStarInfo(703, "No Deaths", StarType.NoDeaths),
            GameStarInfo(704, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(705, "Find the Mini Rocco", StarType.Comic),
            GameStarInfo(706, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Rocco's Rumpus Room", CourseType.Standard, [
            GameStarInfo(710, "Complete the course", StarType.CourseComplete),
            GameStarInfo(711, "Complete in under 02:20", StarType.MinTime),
            GameStarInfo(712, "Complete in under 00:45", StarType.MinTime),
            GameStarInfo(713, "Spend less than 24 seconds on the ground", StarType.Challenge),
            GameStarInfo(714, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(715, "Find the Mini Rocco", StarType.Comic),
            GameStarInfo(716, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Employees Only", CourseType.Standard, [
            GameStarInfo(720, "Complete the course", StarType.CourseComplete),
            GameStarInfo(721, "Complete in under 04:20", StarType.MinTime),
            GameStarInfo(722, "Complete in under 01:20", StarType.MinTime),
            GameStarInfo(723, "No Deaths", StarType.NoDeaths),
            GameStarInfo(724, "Find and open all the gas valves", StarType.Challenge),
            GameStarInfo(725, "Find the Mini Rocco", StarType.Comic),
            GameStarInfo(726, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Storage Room Spree", CourseType.Standard, [
            GameStarInfo(730, "Complete the course", StarType.CourseComplete),
            GameStarInfo(731, "Complete in under 02:00", StarType.MinTime),
            GameStarInfo(732, "Complete in under 00:45", StarType.MinTime),
            GameStarInfo(733, "Find and open all the gas valves", StarType.Challenge),
            GameStarInfo(734, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(735, "Find the Mini Rocco", StarType.Comic),
            GameStarInfo(736, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Birthday Blowout", CourseType.Standard, [
            GameStarInfo(740, "Complete the course", StarType.CourseComplete),
            GameStarInfo(741, "Complete in under 03:00", StarType.MinTime),
            GameStarInfo(742, "Complete in under 00:50", StarType.MinTime),
            GameStarInfo(743, "Find and open all the gas valves", StarType.Challenge),
            GameStarInfo(744, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(745, "No Deaths", StarType.NoDeaths),
            GameStarInfo(746, "Buddy Mode", StarType.Buddy),
        ]),
        GameCourseInfo("Chase to the Arcade", CourseType.Standard, [
            GameStarInfo(750, "Complete the course", StarType.CourseComplete),
            GameStarInfo(751, "Complete in under 00:55", StarType.MinTime),
            GameStarInfo(752, "Complete in under 00:35", StarType.MinTime),
            GameStarInfo(753, "Tag your sister", StarType.Challenge),
            GameStarInfo(754, "Grab the golden pin", StarType.GoldenPin),
            GameStarInfo(755, "Find the Mini Rocco", StarType.Comic),
            GameStarInfo(756, "Where's Buddy?", StarType.BuddyChase),
        ]),
        GameCourseInfo("Pogo Trial 1", CourseType.Pogo, [
            GameStarInfo(760, "Find all the checkpoints using the Pogo Stick", StarType.TrialComplete),
        ]),
        GameCourseInfo("Pogo Trial 2", CourseType.Pogo, [
            GameStarInfo(761, "Find all the checkpoints using the Pogo Stick", StarType.TrialComplete),
        ]),
        GameCourseInfo("Tiny Toy Trial 1", CourseType.TinyToy, [
            GameStarInfo(762, "Get to the finish line", StarType.TrialComplete),
        ]),
        GameCourseInfo("Tiny Toy Trial 2", CourseType.TinyToy, [
            GameStarInfo(763, "Get to the finish line", StarType.TrialComplete),
        ]),
        GameCourseInfo("Jetpack Trial", CourseType.Jetpack, [
            GameStarInfo(764, "Find all the checkpoints using the Jetpack", StarType.TrialComplete),
        ]),
        GameCourseInfo("All Course Marathon", CourseType.AllCourseMarathon, [
            GameStarInfo(765, "Complete the course", StarType.TrialComplete),
        ]),
    ]
)

game_world_dict: dict[str, GameWorldInfo] = {
    gym_class.name: gym_class,
    playground.name: playground,
    school.name: school,
    wholesale.name: wholesale,
    master_class.name: master_class,
    basement.name: basement,
    roccos_arcade.name: roccos_arcade,
}