import unittest

from aocd.models import Puzzle

from y2022.day07 import solve_a, solve_b, ROOT_NAME, FileSystemNode
from y2022.day07 import FileSystemNav

FS_NODE_TEST_NAME = "nodename"

YEAR = 2022
DAY = 7
EXAMPLE_RESULT_A = 95437
EXAMPLE_RESULT_B = 9999

puzzle = Puzzle(year=YEAR, day=DAY)
EXAMPLE_DATA = puzzle.example_data

class TestFileSystemNav(unittest.TestCase):

    def setUp(self) -> None:
        self.fs = FileSystemNav(root = ROOT_NAME)

    def test_pwd_is_root(self):
        self.assertEqual(ROOT_NAME, self.fs.pwd)


class TestFileSytemNode(unittest.TestCase):

    def setUp(self) -> None:
        self.n = FileSystemNode(FS_NODE_TEST_NAME)

    def test_name_returns_name(self):
        self.assertEqual(FS_NODE_TEST_NAME, self.n.name)

class TestDay07(unittest.TestCase):

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
