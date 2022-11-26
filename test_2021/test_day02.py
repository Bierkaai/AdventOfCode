import unittest

from aocd.models import Puzzle

from y2021.day02 import solve_a, solve_b, Submarine

EXAMPLE_RESULT_A = 150
EXAMPLE_RESULT_B = 0


class TestSubmarine(unittest.TestCase):

    def setUp(self) -> None:
        self.sub = Submarine()

    def test_parse_forward_command(self):
        self.sub.parse_command("forward 4")
        self.assertEqual(self.sub.position, 4, f"Sub should have move forward to pos 4, position = {self.sub.position}")

    def test_parse_down_command(self):
        self.sub.parse_command("down 5")
        self.assertEqual(self.sub.depth, 5, f"Sub should be at depth 5, depth = {self.sub.depth}")

    def test_parse_up_command(self):
        self.sub.parse_command("down 4")
        self.sub.parse_command("up 3")
        self.assertEqual(self.sub.depth, 1, f"Sub should be at depth 1, depth = {self.sub.depth}")

    def test_return_multiplied_position_indicator(self):
        self.sub.position = 4
        self.sub.depth = 5
        self.assertEqual(self.sub.multiplied_pos_indicator, 20,
                         f"Sub's position indicator should be 20, not {self.sub.multiplied_pos_indicator}")


class TestDay01(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        puzzle = Puzzle(year=2021, day=2)
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
