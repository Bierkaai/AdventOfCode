import re

from aocd.models import Puzzle

DAY = 6
YEAR = 2023


def build_boatracelist(raw_data):
    for line in raw_data.split("\n"):
        if line.startswith("Time:"):
            times = re.findall(r"[0-9]+", line)
        elif line.startswith("Distance:"):
            dists = re.findall(r"[0-9]+", line)
    return tuple(zip(map(int, times), map(int, dists)))


def solve_a(data):
    races = build_boatracelist(data)
    return 0


def solve_b(data):
    return 0


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
