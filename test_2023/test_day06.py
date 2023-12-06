import unittest

from aocd.models import Puzzle

from y2023.day06 import solve_a, solve_b, build_boatracelist

YEAR = 2023
DAY = 6
EXAMPLE_RESULT_A = 4361
EXAMPLE_RESULT_B = 281

puzzle = Puzzle(year=YEAR, day=DAY)
EXAMPLE_DATA = puzzle.example_data

EXAMPLE_RACECOUNT = 3

EXAMPLE_RACES = (
    (7, 9),
    (15, 40),
    (30, 200)
)


class TestParsing(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.boatraces = build_boatracelist(EXAMPLE_DATA)

    def testRaceCountCorrect(self):
        """There should be three races in the parsed data"""
        self.assertEqual(len(self.boatraces), EXAMPLE_RACECOUNT)

    def testRaceParameters(self):
        for i, subrace in enumerate(EXAMPLE_RACES):
            with self.subTest(i=i):
                self.assertTupleEqual(self.boatraces[i], subrace)


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
