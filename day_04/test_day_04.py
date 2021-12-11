from unittest import TestCase, skip

from day_04 import load, solve, parse_line, find_last_winner

EXAMPLE_FILE = '../input/04example.txt'
DRAW_LIST = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
CORRECT_N_OF_BOARDS = 3
BOARD_SIZE = 5


class TestInput(TestCase):
    # given an input file

    def setUp(self) -> None:
        self.result = load(EXAMPLE_FILE)
        self.drawlist = self.result[0]
        self.boardlist = self.result[1]

    def test_load(self):
        # should return 2 items
        self.assertEqual(len(self.result), 2, "load should return a tuple of length 2")

    def test_draw_list(self):
        # List should match draw list
        self.assertLessEqual(DRAW_LIST, self.drawlist)

    def test_board_list_len(self):
        # test that we get enough boards
        self.assertEqual(CORRECT_N_OF_BOARDS, len(self.boardlist))

    def test_board_list_in_list(self):
        # Test that each board consists of 5 lists of len 5
        n_of_boards = len(self.boardlist)
        for i, board in enumerate(self.boardlist):
            self.assertEqual(BOARD_SIZE, len(board), f"board {i + 1} of {n_of_boards} has wrong number of rows")
            for j, row in enumerate(board):
                self.assertEqual(BOARD_SIZE, len(row), f"row {j + 1} on board {i + 1} has wrong number of entries")


class TestExampleSolution(TestCase):
    # test whether correct output is returned on example case

    def setUp(self) -> None:
        self.result = solve(*load(EXAMPLE_FILE))
        self.desired_result = 4512

    def test_solve(self):
        self.assertEqual(self.desired_result, self.result)

class TestSecondPartExample(TestCase):
    def setUp(self) -> None:
        self.result = find_last_winner(*load(EXAMPLE_FILE))
        self.desired_result = 1924

    def test_last_winner(self):
        self.assertEqual(self.desired_result, self.result)

class TestLineParser(TestCase):

    def test_parse_line(self):
        result = parse_line("0 3 2 4 5")
        self.assertEqual(result, [0, 3, 2, 4, 5])

    def test_parse_line_with_double_spaces(self):
        result = parse_line("0  3 2 4 5")
        self.assertEqual(result, [0, 3, 2, 4, 5])

    def test_parse_line_with_trailing_whitespace(self):
        result = parse_line("0 3 2 4 5  ")
        self.assertEqual(result, [0, 3, 2, 4, 5])
