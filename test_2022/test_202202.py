import unittest

from aocd.models import Puzzle

from y2022.day02 import solve_a, solve_b
from y2022.day02 import parse_strategy_guide_a, calculate_move_score, parse_strategy_guide_b

YEAR = 2022
DAY = 2
EXAMPLE_RESULT_A = 15
EXAMPLE_RESULT_B = 12

puzzle = Puzzle(year=YEAR, day=DAY)
EXAMPLE_DATA = puzzle.example_data

EXAMPLE_DATA_PARSED = [
    ('R', 'P'),
    ('P', 'R'),
    ('S', 'S')
]


MORE_EXAMPLE_PARSING = """A X
B X
C X
B Y
C Z
"""

MORE_EXAMPLE_PARSED_B = [
    ('R', 'S'),
    ('P', 'R'),
    ('S', 'P'),
    ('P', 'P'),
    ('S', 'R')
]

MORE_EXAMPLE_PARSED = [
    ('R', 'R'),
    ('P', 'R'),
    ('S', 'R'),
    ('P', 'P'),
    ('S', 'S')
]


MORE_EXAMPLE_SOLVED_SCORE = (
    1 + 3 +
    1 + 0 +
    1 + 6 +
    2 + 3 +
    3 + 3
)

# Rock = 1, Paper = 2, Scissors = 3
# Win = 6, draw = 3, loss = 0

MOVE_SCORE_TUPLES = [
    (('R', 'P'), 8),
    (('P', 'R'), 1),
    (('S', 'P'), 2),
    (('S', 'S'), 6),
    (('P', 'P'), 5)
]


# This can be done with a simple lookup dict, but probably part B needs actual implementaton

class TestCalculateScore(unittest.TestCase):

    def test_parse_input(self):
        output = parse_strategy_guide_a(EXAMPLE_DATA)
        self.assertListEqual(EXAMPLE_DATA_PARSED, output)

    def test_parse_input_2(self):
        output = parse_strategy_guide_a(MORE_EXAMPLE_PARSING)
        self.assertListEqual(MORE_EXAMPLE_PARSED, output)

    def test_calculate_score(self):
        for i, tup in enumerate(MOVE_SCORE_TUPLES):
            move, score = tup
            with self.subTest(i=i):
                self.assertEqual(score, calculate_move_score(move), f"Score for move {move} should be {score}")

    def test_parse_strategy_guide_b(self):
        output = parse_strategy_guide_b(MORE_EXAMPLE_PARSING)
        self.assertListEqual(MORE_EXAMPLE_PARSED_B, output)


class TestSolver(unittest.TestCase):

    def test_solve_bigger_example(self):
        self.assertEqual(solve_a(MORE_EXAMPLE_PARSING), MORE_EXAMPLE_SOLVED_SCORE)


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
