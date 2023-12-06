import re

from aocd.models import Puzzle

DAY = 5
YEAR = 2023


class Almanac:

    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.parse(raw_data)

    def parse(self, raw_data):
        for line in raw_data.split('\n'):
            if line.startswith("seeds"):
                match = re.match(r"(?:seeds\:)((?:\s*[0-9]+)+)", line)
                self.seed_list = list(map(int, match.group(1).split()))


def solve_a(data):
    return None


def solve_b(data):
    return None


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
