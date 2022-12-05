import unittest

from aocd.models import Puzzle

from y2022.day05 import parse_and_split_input, DockCrane, DockCrane9001, parse_move_instruction
from y2022.day05 import solve_a, solve_b

YEAR = 2022
DAY = 5
EXAMPLE_RESULT_A = "CMZ"
EXAMPLE_RESULT_B = "MCD"

puzzle = Puzzle(year=YEAR, day=DAY)
EXAMPLE_DATA = puzzle.example_data

EXAMPLE_DOCK = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3 "
]

EXAMPLE_MOVE = "move 2 from 1 to 3"
EXAMPLE_MOVE_PARSED = (2, 1, 3)

EXAMPLE_MOVES = ["move 1 from 2 to 1", "move 3 from 1 to 3", "move 2 from 2 to 1", "move 1 from 1 to 2"]
DOCK = {1: ["N", "Z"],
        2: ["D", "C", "M"],
        3: ["P"]
        }

EXAMPLE_DOCK_MOVE_1_FROM_2_TO_3 = {
    1: ["N", "Z"],
    2: ["C", "M"],
    3: ["D", "P"]
}

EXAMPLE_DOCK_MOVE_2_FROM_1_TO_3 = {
    1: [],
    2: ["D", "C", "M"],
    3: ["Z", "N", "P"]
}

EXAMPLE_DOCK_MOVE_2_FROM_1_TO_3_9001 = {
    1: [],
    2: ["D", "C", "M"],
    3: ["N", "Z", "P"]
}

EXAMPLE_READ_TOPLINE = "NDP"


class TestParser(unittest.TestCase):

    def setUp(self):
        self.dock, self.moves = parse_and_split_input(EXAMPLE_DATA)

    def test_parse_split_dock_on_newline(self):
        self.assertEqual(EXAMPLE_DOCK, self.dock)

    def test_parse_split_moves_on_newLine(self):
        self.assertEqual(EXAMPLE_MOVES, self.moves)

    def test_parse_move_instruction(self):
        output_move_parsed = parse_move_instruction(EXAMPLE_MOVE)
        self.assertTupleEqual(EXAMPLE_MOVE_PARSED, output_move_parsed)


class TestCrane9001(unittest.TestCase):

    def setUp(self) -> None:
        self.dc = DockCrane9001(EXAMPLE_DOCK)

    def test_move_two_crates(self):
        self.dc.move(n=2, source=1, target=3)
        self.assertDictEqual(EXAMPLE_DOCK_MOVE_2_FROM_1_TO_3_9001, self.dc.dock)

    def test_move_single_crate(self):
        self.dc.move(n=1, source=2, target=3)
        self.assertDictEqual(EXAMPLE_DOCK_MOVE_1_FROM_2_TO_3, self.dc.dock)


class TestCrane(unittest.TestCase):

    def setUp(self) -> None:
        self.dc = DockCrane(EXAMPLE_DOCK)

    def test_dock_parsing(self):
        self.assertDictEqual(DOCK, self.dc.dock)

    def test_read_topline(self):
        self.assertEqual(EXAMPLE_READ_TOPLINE, self.dc.read_topline())

    def test_move_single_crate(self):
        self.dc.move(n=1, source=2, target=3)
        self.assertDictEqual(EXAMPLE_DOCK_MOVE_1_FROM_2_TO_3, self.dc.dock)

    def test_move_two_crates(self):
        self.dc.move(n=2, source=1, target=3)
        self.assertDictEqual(EXAMPLE_DOCK_MOVE_2_FROM_1_TO_3, self.dc.dock)

    def test_do_move_from_str(self):
        self.dc.move_from_str(EXAMPLE_MOVE)
        self.assertDictEqual(EXAMPLE_DOCK_MOVE_2_FROM_1_TO_3, self.dc.dock)


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
