import numpy as np
from aocd.models import Puzzle

DAY = 6
YEAR = 2022

def find_first_marker(character_str, n=4):
    last_n_characters = []
    for i, char in enumerate(character_str):
        last_n_characters.append(char)
        if len(last_n_characters) > n:
            last_n_characters.pop(0)
        if len(set(last_n_characters)) == n:
            return i + 1
    return None


def solve_a(data):
    return find_first_marker(data)



def solve_b(data):
    return find_first_marker(data, 14)



if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
