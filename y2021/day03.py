from abc import ABC, abstractmethod
from dataclasses import dataclass

from aocd.models import Puzzle

DAY = 3
YEAR = 2021


def solve_a(data):
    return None

def solve_b(data):
    return None


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
