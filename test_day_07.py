from unittest import TestCase

from day_07 import CrabSolver, triangular, CrabSolverRework, AbstractCrabSolver

FUEL_TO_POS_3 = 39

TEST_POSITIONS = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
TEST_OUTCOME = 37


class CrabSolverTester(TestCase):

    def setUp(self) -> None:
        self.cs = AbstractCrabSolver(TEST_POSITIONS)

    def fuel_to_move_to_pos_x_is_y(self, x, y):
        # function to run test cases
        fuel = self.cs.fuel_to_pos(x)
        self.assertEqual(y, fuel, f"It should take {y} fuel to go to position {x}")


class TestCrabSolver(CrabSolverTester):

    def setUp(self) -> None:
        self.cs = CrabSolver(TEST_POSITIONS)

    def test_fuel_to_move_to_position_3_is_39(self):
        self.fuel_to_move_to_pos_x_is_y(3, 39)

    def test_fuel_to_move_to_position_1_is_41(self):
        self.fuel_to_move_to_pos_x_is_y(1, 41)

    def test_fuel_to_move_to_position_10_is_71(self):
        self.fuel_to_move_to_pos_x_is_y(10, 71)

    def test_minimal_fuel_is_correct_to_example_outcome(self):
        fuel = self.cs.minimal_fuel()
        self.assertEqual(TEST_OUTCOME, fuel)


class TestCrabSolverRework(CrabSolverTester):

    def setUp(self) -> None:
        self.cs = CrabSolverRework(TEST_POSITIONS)

    def test_fuel_to_position_2_is_206(self):
        self.fuel_to_move_to_pos_x_is_y(2, 206)

    def test_minimal_fuel_is_168(self):
        self.assertEqual(168, self.cs.minimal_fuel())

class TestTriangular(TestCase):

    def test_triangular_1(self):
        self.assertEqual(triangular(1), 1)

    def test_triangular_2_is_3(self):
        self.assertEqual(triangular(2), 3)
