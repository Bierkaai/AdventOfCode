import unittest
from unittest.mock import patch, MagicMock

import numpy as np
from aocd.models import Puzzle

from y2022.day19 import solve_a, solve_b, parse_blueprint, dfsbots

YEAR = 2022
DAY = 19
EXAMPLE_RESULT_A = 3096
EXAMPLE_RESULT_B = 9999

puzzle = Puzzle(year=YEAR, day=DAY)
EXAMPLE_DATA = puzzle.example_data

EXAMPLE_BLUEPRINT = "Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. " + \
                    "Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian."

EXAMPLE_BP_NO = 1
EXAMPLE_ROBOT_COSTS = {
    "ore": {"ore": 4},
    "clay": {"ore": 2},
    "obsidian": {"ore": 3,
                 "clay": 14},
    "geode": {"ore": 2,
              "obsidian": 7},
}

EX_BP_TUP = (
    np.array((4, 0, 0, 0), dtype=int),
    np.array((2, 0, 0, 0), dtype=int),
    np.array((3, 14, 0, 0), dtype=int),
    np.array((2, 0, 7, 0), dtype=int)
)

EX_START_INVENT = np.array((1, 0, 0, 0), dtype=int)
EX_START_RESOURCES = np.array((0, 0, 0, 0), dtype=int)


class TestDFSOneStep(unittest.TestCase):

    @patch("y2022.day19.dfsbots")
    def test_DFS_builds_clay_bot_after_3_minutes(self, mockfun: MagicMock):
        _ = dfsbots(time_left=3,
                    blueprint=EX_BP_TUP,
                    inventory=EX_START_INVENT,
                    resources=EX_START_RESOURCES)
        mockfun.assert_called_with(
            time_left=0,
            blueprint=EX_BP_TUP,
            inventory=(1, 1, 0, 0),
            resources=(1, 0, 0, 0)
        )


class TestBlueprintParser(unittest.TestCase):

    def setUp(self) -> None:
        self.blueprint_id, self.botcosts = parse_blueprint(EXAMPLE_BLUEPRINT)

    def test_id_number_parsed(self):
        self.assertEqual(EXAMPLE_BP_NO, self.blueprint_id)

    def test_cost_parser(self):
        for robot_type, expected_costs in EXAMPLE_ROBOT_COSTS.items():
            with self.subTest(msg=f"Testing costs for {robot_type} robot"):
                self.assertDictEqual(expected_costs, self.botcosts[robot_type])


class TestDay19(unittest.TestCase):

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
