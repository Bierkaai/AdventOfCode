import types

from aocd.models import Puzzle

DAY = 1
YEAR = 2022


def tokenize(input: str) -> types.GeneratorType:
    buffer = []
    for line in input.splitlines(keepends=False):
        if len(line) == 0:
            yield buffer
            buffer = []
        else:
            buffer.append(int(line))
    yield buffer


def max_sum(list_of_list, n=1):
    summed = [sum(l) for l in list_of_list]
    return sum(sorted(summed, reverse=True)[:n])


def solve_a(data):
    return max_sum(tokenize(data))


def solve_b(data):
    return max_sum(tokenize(data), n=3)


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
