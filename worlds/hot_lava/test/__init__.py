from test.bases import WorldTestBase


class HotLavaTestBase(WorldTestBase):
    game = "Hot Lava"


class HotLavaAllStarsTestBase(WorldTestBase):
    game = "Hot Lava"
    options = {
        "enable_all_course_stars": 1,
    }
