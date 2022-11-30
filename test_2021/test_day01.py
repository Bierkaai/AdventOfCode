import unittest

from aocd.models import Puzzle

from y2021.day01 import parse_list_str_to_list_int, count_total_increases_in_list
from y2021.day01 import solve_a, solve_b

YEAR = 2021
DAY = 1
EXAMPLE_RESULT_A = 7
EXAMPLE_RESULT_B = 5

puzzle = Puzzle(year=YEAR, day=DAY)
EXAMPLE_DATA = puzzle.example_data

LIST_OF_STR = """
123
122
555
"""

INT_LIST = [123, 122, 555]
INCREASES = 1


class TestFunctionality(unittest.TestCase):

    def test_parse_list_str_to_list_int(self):
        result = parse_list_str_to_list_int(LIST_OF_STR)
        self.assertListEqual(INT_LIST, result)

    def test_count_total_increase(self):
        result = count_total_increases_in_list(INT_LIST)
        self.assertEqual(INCREASES, result)




if __name__ == '__main__':
    unittest.main()
