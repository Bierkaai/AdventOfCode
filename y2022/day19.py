

from aocd.models import Puzzle


DAY = 19
YEAR = 2022

class RobotBuilderSimulator:

    def __init__(self, blueprint: str):
        self.parse_blueprint(blueprint)

    def parse_blueprint(self, blueprint):
        id_str, costs_str = blueprint.split(":")
        self.blueprint_id = int(id_str.split(" ")[1])


def solve_a(data):
    pass


def solve_b(data):
    pass


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)


