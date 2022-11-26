import unittest

from aocd.models import Puzzle

from y2021.day01 import parse_list_str_to_list_int, count_total_increases_in_list
from y2021.day01 import solve_a, solve_b

EXAMPLE_RESULT_A = 7
EXAMPLE_RESULT_B = 5

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


class TestDay01(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        puzzle = Puzzle(year=2021, day=1)
        cls.example_data = puzzle.example_data
        cls.example_result_a = EXAMPLE_RESULT_A
        cls.example_result_b = EXAMPLE_RESULT_B

    def test_example_a(self):
        result = solve_a(self.example_data)
        self.assertEqual(self.example_result_a, result, f"Example result should be {self.example_result_a}, not {result}")

    def test_example_b(self):
        result = solve_b(self.example_data)
        self.assertEqual(self.example_result_b, result, f"Example result B should be {self.example_result_b}, not {result}")


if __name__ == '__main__':
    unittest.main()
