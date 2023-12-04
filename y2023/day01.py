import re

from aocd.models import Puzzle

PATTERN_B = r"([0-9]|one|two|three|four|five|six|seven|eight|nine){1}"
PATTERN_A = r"[0-9]{1}"

DAY = 1
YEAR = 2023

WORD_DIGITS = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]

digit_map = dict(zip(WORD_DIGITS, range(1, 10)))


def find_all_numbers(string: str, allow_written=False) -> list[str]:
    pattern = PATTERN_B if allow_written else PATTERN_A
    return re.findall(pattern, string)


def parse_to_int(str_digit: str) -> int:
    try:
        return int(str_digit)
    except ValueError:
        if str_digit in digit_map:
            return digit_map[str_digit]
    raise ValueError(f"Cannot parse {str_digit} to digit.")


def create_digit_list(digit_str: list[str]) -> list[int]:
    return list(map(parse_to_int, digit_str))


def create_number(digit_list: list[int]) -> int:
    first = digit_list[0]
    last = digit_list[-1]
    return int(str(first) + str(last))


def solve(data, allow_written=False):
    result_sum = 0
    for line in data.split("\n"):
        digits_list = create_digit_list(find_all_numbers(line, allow_written))
        result_sum += create_number(digits_list)
    return result_sum


def solve_a(data):
    return solve(data)


def solve_b(data):
    return solve(data, allow_written=True)


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
