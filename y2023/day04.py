import re
from aocd.models import Puzzle

DAY = 4
YEAR = 2023

PATTERN = r"(?:Card\s?)([0-9]+)(?:\:)((?:\s+[0-9]+)+)(?:\s+\|)((?:\s+[0-9]+)+)"

class Card:

    card_nr: int

    def __init__(self, data):
        self.raw_data = data
        self.cardnr, self.winning, self.you_have = self.parse_input(data)

    def parse_input(self, input_data: str):
        def parse_to_list_of_int(list_of_nr_str: list[str]) -> list[int]:
            return list(map(int, list_of_nr_str))

        matches = re.match(PATTERN, input_data)
        nr = int(matches.group(1))
        winning = parse_to_list_of_int(matches.group(2).split())
        you_have = parse_to_list_of_int(matches.group(3).split())
        return nr, winning, you_have

def solve_a(data):
    return None


def solve_b(data):
    return None


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
