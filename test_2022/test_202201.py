import types
import unittest

from aocd.models import Puzzle

from y2022.day01 import solve_a, solve_b
from y2022.day01 import tokenize, max_sum

YEAR = 2022
DAY = 1
EXAMPLE_RESULT_A = 24000
EXAMPLE_RESULT_B = 45000

puzzle = Puzzle(year=YEAR, day=DAY)
EXAMPLE_DATA = puzzle.example_data

EXAMPLE_INPUT = """1000
2000

4000

2000
"""

TOKENIZED = [[1000, 2000], [4000, ], [2000, ]]
MAX_SUM = 4000
TOP_2_SUM = 7000

TOKENIZED_MORE = [
    [100, 100],
    [400, 300],
    [200],
    [100, 100, 100],
    [200, 400, 400]
]

TOP_3_SUM = 2000


class TestItemizer(unittest.TestCase):

    def test_tokenizer_returns_generator(self):
        self.assertIsInstance(tokenize(EXAMPLE_DATA), types.GeneratorType)

    def test_tokenization(self):
        output = list(tokenize(EXAMPLE_INPUT))
        self.assertListEqual(TOKENIZED, output)


class TestMaxSummer(unittest.TestCase):

    def test_return_max_sum(self):
        output = max_sum(TOKENIZED)
        self.assertEqual(MAX_SUM, output)

    def test_return_max_sum_top_2(self):
        output = max_sum(TOKENIZED, n=2)
        self.assertEqual(TOP_2_SUM, output)

    def test_return_max_sum_top_3(self):
        output = max_sum(TOKENIZED_MORE, n=3)
        self.assertEqual(TOP_3_SUM, output)



class TestDay01(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        puzzle = Puzzle(year=YEAR, day=DAY)
        cls.example_data = puzzle.example_data
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
