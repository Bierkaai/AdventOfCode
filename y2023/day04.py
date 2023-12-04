import re

from aocd.models import Puzzle

DAY = 4
YEAR = 2023

PATTERN = r"(?:Card\s+)([0-9]+)(?:\:)((?:\s+[0-9]+)+)(?:\s+\|)((?:\s+[0-9]+)+)"


class Card:
    cardnr: int
    winning: set
    you_have: set
    matched: set
    score: int

    def __init__(self, data):
        self.raw_data = data
        self.cardnr, self.winning, self.you_have = self.parse_input(data)

    def parse_input(self, raw_data_str: str) -> tuple[int, set, set]:
        def parse_to_list_of_int(list_of_nr_str: list[str]) -> list[int]:
            return list(map(int, list_of_nr_str))

        matches = re.match(PATTERN, raw_data_str)
        try:
            nr = int(matches.group(1))
            winning = set(parse_to_list_of_int(matches.group(2).split()))
            you_have = set(parse_to_list_of_int(matches.group(3).split()))
        except AttributeError:
            raise AttributeError(f"Parsing failed for string? '{raw_data_str}'")
        return nr, winning, you_have

    @property
    def matched(self) -> set:
        return self.you_have & self.winning

    @property
    def score(self) -> int:
        count = len(self.matched)
        if count == 0:
            return 0
        return 2 ** (count - 1)

    def __add__(self, other) -> int:
        return int(self) + int(other)

    def __int__(self) -> int:
        return self.score


def generate_cards(raw_data):
    yield from map(Card, raw_data.split("\n"))


def get_total_card_count_from_score_list(score_list: list[int]) -> int:
    if len(score_list) == 0:
        return 0
    if len(score_list) == 1:
        return 1
    return 0


def solve_a(data):
    cards = list(generate_cards(data))
    scores = map(int, cards)
    return sum(scores)


def solve_b(data):
    return None


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
