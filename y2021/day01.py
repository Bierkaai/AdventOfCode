import numpy as np
from aocd.models import Puzzle

DAY = 1
YEAR = 2021

def parse_list_str_to_list_int(list_str: str) -> list:
    return [int(x) for x in list_str.split()]

def count_total_increases_in_list(list_nums: list) -> int:
    return (np.diff(np.array(list_nums)) > 0).sum()

def solve_a(data):
    parsed = parse_list_str_to_list_int(data)
    return count_total_increases_in_list(parsed)

def solve_b(data):
    parsed = parse_list_str_to_list_int(data)
    window_size = 3

    # we only need to check if the newly added number is higher than
    # the removed number
    total_window_sum_increases = 0
    first_number_previous_window = parsed[0]

    for i in range(1, len(parsed) - window_size + 1):
        if parsed[i + window_size - 1] > first_number_previous_window:
            total_window_sum_increases += 1
        first_number_previous_window = parsed[i]

    return total_window_sum_increases

if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)


