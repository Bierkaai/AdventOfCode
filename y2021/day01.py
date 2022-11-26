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

    # we only need to check if the first item of the previous window
    # is lower than the last item in the new window

    # first item of previous window for all windows except first
    first_items = parsed[:-window_size]

    # last item of current window for all windows except first
    last_items = parsed[window_size:]

    # zipping the two lists to item-by-item check if added item is larger than removed one
    # Using upcast of boolean True to integer 1 to count
    return sum(f < l for f, l in zip(first_items, last_items))


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)


