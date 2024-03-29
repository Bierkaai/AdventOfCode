import unittest

from aocd.models import Puzzle

from y2023.day05 import solve_a, solve_b, Almanac

YEAR = 2023
DAY = 5
EXAMPLE_RESULT_A = 35
EXAMPLE_RESULT_B = 281

puzzle = Puzzle(year=YEAR, day=DAY)
EXAMPLE_DATA = puzzle.example_data

EXAMPLE_SEEDS = [79, 14, 55, 13]
SEED_TO_SOIL = [(50, 98, 2), (52, 50, 48)]


class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.a = Almanac(EXAMPLE_DATA)

    def test_seed_list(self):
        self.assertListEqual(self.a.seed_list, EXAMPLE_SEEDS)


class TestDay01(unittest.TestCase):

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
