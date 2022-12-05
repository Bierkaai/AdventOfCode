import unittest

from aocd.models import Puzzle

from y2022.day04 import make_set, make_two_sets, fully_contains
from y2022.day04 import solve_a, solve_b, overlaps

YEAR = 2022
DAY = 4
EXAMPLE_RESULT_A = 2
EXAMPLE_RESULT_B = 4

puzzle = Puzzle(year=YEAR, day=DAY)
EXAMPLE_DATA = puzzle.example_data

FIRST_LINE = "2-4,6-8"
FIRST_LINE_SETS = ({2, 3, 4}, {6, 7, 8})

SIMPLE_RANGE_STR = "4-9"
SIMPLE_RANGE_SET = {4, 5, 6, 7, 8, 9}

SUBSET_TESTS = [
    ([{2, 3, 4}, {2, 3}], True),
    ([{7, 8}, {3, 4, 5, 6, 7, 8, 9}], True),
    ([{6, 7}, {3, 4, 5, 6, 7, 8}], True),
    ([{1, 2, 3}, {4, 5, 6}], False),
    ([{1, 2, 3}, {1, 2, 3}], True)
]

OVERLAPS_TESTS = [
    ([{1, 2, 3}, {3, 4, 5}], True),
]


class TestSectionLogic(unittest.TestCase):

    def test_parse_input(self):
        self.assertTupleEqual(FIRST_LINE_SETS, make_two_sets(FIRST_LINE))

    def test_make_set(self):
        self.assertSetEqual(SIMPLE_RANGE_SET, make_set(SIMPLE_RANGE_STR))

    def test_determine_subsets(self):
        self.assertTrue(fully_contains({2, 3, 4}, {2, 3}))
        for i, testcase in enumerate(SUBSET_TESTS):
            with self.subTest(i=i):
                case, expected_result = testcase
                self.assertEqual(expected_result, fully_contains(*case))

    def test_overlap(self):
        for i, testcase in enumerate(SUBSET_TESTS + OVERLAPS_TESTS):
            with self.subTest(i=i):
                case, expected_result = testcase
                self.assertEqual(expected_result, overlaps(*case))


class TestDay04(unittest.TestCase):

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
