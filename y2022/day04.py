from aocd.models import Puzzle

DAY = 4
YEAR = 2022


def make_set(input_range_str):
    start, end = (int(x) for x in input_range_str.split("-"))
    return set(range(start, end + 1))


def make_two_sets(input_line):
    return tuple(make_set(rng) for rng in input_line.split(','))


def fully_contains(set_1: set, set_2: set) -> bool:
    """
    Tests whether one set fully contains another set, bidirectionally

    :param set_1: a set
    :param set_2: another set
    :return: True if either set fully contains the other
    """
    if set_1 <= set_2:
        return True
    if set_2 <= set_1:
        return True
    return False


def overlaps(set_1: set, set_2: set) -> bool:
    return not set_1.isdisjoint(set_2)


def solver(data, fun):
    return sum([
        fun(*make_two_sets(line))
        for line in data.splitlines(keepends=False)
    ])


def solve_a(data):
    return solver(data, fully_contains)


def solve_b(data):
    return solver(data, overlaps)


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
