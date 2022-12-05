import numpy as np
from aocd.models import Puzzle

DAY = 2
YEAR = 2022

moves = ["R", "P", "S"]
mapping = dict(zip(["A", "B", "C", "X", "Y", "Z"], moves * 2))

MOVE_SCORES = dict(zip(moves, (x + 1 for x in range(3))))

WINNING_COMBINATIONS = (("S", "R"), ("R", "P"), ("P", "S"))


def parse_strategy_guide(raw_data: str):
    return [tuple(mapping[x] for x in line.split()) for line in raw_data.splitlines(keepends=False)]


def calculate_move_score(move):
    their_move, my_move = move
    my_score = MOVE_SCORES[my_move]
    if my_move == their_move:
        return my_score + 3
    if move in WINNING_COMBINATIONS:
        return my_score + 6
    return my_score


def solve_a(data):
    return sum(calculate_move_score(m) for m in parse_strategy_guide(data))


def solve_b(data):
    pass


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
