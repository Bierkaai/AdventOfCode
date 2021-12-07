from collections import Iterable
from unittest import TestCase

from bingoboard import BingoBoard, transpose

TEST_NR_NOT_IN_BOARD = 27

TEST_NR_IN_BOARD = 22

TEST_DECREASE = 11

TEST_BOARD = [
    [22, 13, 17, 11, 0],
    [8, 2, 23, 4, 24],
    [21, 9, 14, 16, 7],
    [6, 10, 3, 18, 5],
    [1, 12, 20, 15, 19]
]

TEST_WIN_COL = [17, 23, 14, 3, 20]
TEST_BAD_ROW = [8, 2, 23, 4, 7]

TEST_BOARD_SIZE: int = len(TEST_BOARD)
TEST_BOARD_SUM: int = sum([sum(r) for r in TEST_BOARD])

TRANSPOSE_INPUT = [
    [1, 2],
    [3, 5]
]
TRANSPOSE_OUTPUT = [
    [1, 3],
    [2, 5]
]


class TestBingoBoard(TestCase):

    def setUp(self):
        self.bb = BingoBoard(TEST_BOARD)

    def test_board_sum(self):
        # Sum should return sum of all non-marked cells
        self.assertEqual(TEST_BOARD_SUM, self.bb.sum)

    def test_sum_decrease(self):
        self.bb.mark(TEST_DECREASE)
        self.assertEqual(TEST_BOARD_SUM - TEST_DECREASE, self.bb.sum)

    def test_sum_unchanged(self):
        self.bb.mark(TEST_NR_NOT_IN_BOARD)
        self.assertEqual(TEST_BOARD_SUM, self.bb.sum)

    def test_contains(self):
        self.assertTrue(TEST_NR_IN_BOARD in self.bb, f"{TEST_NR_IN_BOARD} should be in board")
        self.assertFalse(TEST_NR_NOT_IN_BOARD in self.bb, f"{TEST_NR_NOT_IN_BOARD} should not be in board")

    def test_win_row(self):
        for i in TEST_BOARD[2]:
            self.bb.mark(i)
        self.assertTrue(self.bb.hasWon)

    def test_not_win_crooked_row(self):
        for i in TEST_BAD_ROW:
            self.bb.mark(i)
        self.assertFalse(self.bb.hasWon)

    def test_win_col(self):
        for i in TEST_WIN_COL:
            self.bb.mark(i)
        self.assertTrue(self.bb.hasWon)

class TestTranspose(TestCase):
    def test_transpose(self):
        self.assertListEqual(transpose(TRANSPOSE_INPUT), TRANSPOSE_OUTPUT)
