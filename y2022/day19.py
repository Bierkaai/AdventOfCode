import re
from typing import Dict, Tuple, Any

from aocd.models import Puzzle

DAY = 19
YEAR = 2022

pattern = re.compile(r"(?:Each )([a-z]+)(?: robot costs )((?:[0-9]+ [a-z]+(?: and |\.))+)")
costs_pattern = re.compile(r"([0-9]+ [a-z]+)(?: and |\.)")


def parse_blueprint(blueprint: str) -> tuple[int, dict[Any, dict]]:
    id_str, costs_str = blueprint.split(":")
    blueprint_id = int(id_str.split(" ")[1])

    botcosts = dict()
    matches = pattern.findall(costs_str)
    for robot_type, costs_str in matches:
        botcosts[robot_type] = {x[1]: int(x[0])
                                for x in [match.split() for match in costs_pattern.findall(costs_str)]}
    return blueprint_id, botcosts


def solve_a(data):
    pass


def solve_b(data):
    pass


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
