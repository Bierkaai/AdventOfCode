import unittest

from aocd.models import Puzzle

from y2022.day02 import solve_a, solve_b

YEAR = 2022
DAY = 2
EXAMPLE_RESULT_A = None
EXAMPLE_RESULT_B = None

puzzle = Puzzle(year=YEAR, day=DAY)
EXAMPLE_DATA = puzzle.example_data

class TestDay02(unittest.TestCase):

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
