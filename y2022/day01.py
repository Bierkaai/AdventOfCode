import types

import numpy as np
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
    max_sum = 0
    for subl in list_of_list:
        summed = sum(subl)
        if summed> max_sum:
            max_sum = summed
    return max_sum

def solve_a(data):
    return max_sum(tokenize(data))


def solve_b(data):
    pass


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)


