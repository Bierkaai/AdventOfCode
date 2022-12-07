import unittest

from aocd.models import Puzzle

from y2022.day06 import solve_a, solve_b
from y2022.day06 import find_first_marker

YEAR = 2022
DAY = 6
EXAMPLE_RESULT_A = 7
EXAMPLE_RESULT_B = 19

puzzle = Puzzle(year=YEAR, day=DAY)
EXAMPLE_DATA = puzzle.example_data

EXTRA_EXAMPLE = "bvwbjplbgvbhsrlpgdmjqwftvncz"
FIRST_MARKER = 5
FIRST_14_MARKER = 23


class TestFunctionality(unittest.TestCase):

    def test_find_first_marker(self):
        output = find_first_marker(EXTRA_EXAMPLE)
        self.assertEqual(FIRST_MARKER, output)

    def test_longer_marker_str(self):
        output = find_first_marker(EXTRA_EXAMPLE, n=14)
        self.assertEqual(FIRST_14_MARKER, output)




class TestDay06(unittest.TestCase):

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
