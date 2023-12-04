import unittest

from aocd.models import Puzzle

from y2023.day04 import solve_a, solve_b, Card

YEAR = 2023
DAY = 4
EXAMPLE_RESULT_A = 13
EXAMPLE_RESULT_B = 281

puzzle = Puzzle(year=YEAR, day=DAY)
EXAMPLE_DATA = puzzle.example_data

CARD_EX = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
CARD_NR = 1
WINNING_NUMBERS = [41, 48, 83, 86, 17]
NUMBERS_YOU_HAVE = [83, 86, 6, 31, 17, 9, 48, 53]
MATCHING_NUMBERS = [83, 17, 86, 17]
VALUE = 8


class TestCardHandling(unittest.TestCase):

    def setUp(self) -> None:
        self.card = Card(CARD_EX)

    def test_parsing(self):
        """Test whether the parsing works correctly"""
        self.assertEqual(self.card.cardnr, CARD_NR)
        self.assertListEqual(self.card.winning, WINNING_NUMBERS)
        self.assertListEqual(self.card.you_have, NUMBERS_YOU_HAVE)


class TestDay04(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.example_data = EXAMPLE_DATA
        cls.example_result_a = EXAMPLE_RESULT_A
        cls.example_result_b = EXAMPLE_RESULT_B

    def test_example_a(self):
        result = solve_a(self.example_data)
        self.assertEqual(self.example_result_a, result,
                         f"Example result should be {self.example_result_a}, not {result}")

    def test_example_b(self):
        result = solve_b(self.example_data)
        self.assertEqual(self.example_result_b, result,
                         f"Example result B should be {self.example_result_b}, not {result}")


if __name__ == '__main__':
    unittest.main()
