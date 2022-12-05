import unittest

from aocd.models import Puzzle

from y2021.day03 import solve_a, solve_b
from y2021.day03 import tokenize_to_str_list, transpose_str_list, get_most_common_bit

YEAR = 2021
DAY = 3

EXAMPLE_RESULT_A = 198
EXAMPLE_RESULT_B = 900

EXAMPLE_BITSTRING = "10011"
EXAMPLE_MOST_COMMON_BIT = "1"

EXAMPLE_BITSTRING_2 = "00010"
EXAMPLE_MOST_COMMON_BIT_2 = "0"

SMALL_INPUT_STR = """100
111
100
001
"""

SMALL_INPUT = ["100", "111", "100", "001"]
TRANSPOSE_SMALL = ["1110", "0100", "0101"]


class TestInputParse(unittest.TestCase):

    def test_tokenize_small(self):
        output = tokenize_to_str_list(SMALL_INPUT_STR)
        self.assertListEqual(SMALL_INPUT, output)

    def test_transpose_small(self):
        output = transpose_str_list(SMALL_INPUT)
        self.assertListEqual(TRANSPOSE_SMALL, output)


class TestProcessing(unittest.TestCase):

    def test_get_most_common_bit(self):
        self.assertEqual(EXAMPLE_MOST_COMMON_BIT, get_most_common_bit(EXAMPLE_BITSTRING))

    def test_get_most_common_bit_edge_case(self):
        self.assertEqual(EXAMPLE_MOST_COMMON_BIT_2, get_most_common_bit(EXAMPLE_BITSTRING_2))


class TestDay03(unittest.TestCase):

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
