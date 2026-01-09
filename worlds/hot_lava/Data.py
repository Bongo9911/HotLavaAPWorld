import pkgutil
from typing import Any, Dict, List, Union
import orjson

def load_json_data(data_name: str) -> Union[List[Any], Dict[str, Any]]:
    return orjson.loads(pkgutil.get_data(__name__, "data/" + data_name).decode("utf-8-sig"))

def load_world_data():
    return load_json_data("game_worlds.json")