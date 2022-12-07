import unittest


from aocd.models import Puzzle

from y2022.day07 import solve_a, solve_b, ROOT_NAME, FileSystemNode, File, Directory
from y2022.day07 import FileSystemNav

TEST_FILE_SIZE = 142311

TEST_FILE_NAME = "illegal_download.mov"

FS_NODE_TEST_NAME = "nodename"
FS_SUBDIR = "bla"

YEAR = 2022
DAY = 7
EXAMPLE_RESULT_A = 95437
EXAMPLE_RESULT_B = 9999

puzzle = Puzzle(year=YEAR, day=DAY)
EXAMPLE_DATA = puzzle.example_data


class TestFileSystemNav(unittest.TestCase):

    def setUp(self) -> None:
        self.fs = FileSystemNav(root=ROOT_NAME)
        self.fs.add_file(name=TEST_FILE_NAME, size=TEST_FILE_SIZE)
        self.fs.add_dir(name=FS_SUBDIR)

    def test_pwd_is_root(self):
        self.assertIsInstance(self.fs.pwd, FileSystemNode)
        self.assertEqual(ROOT_NAME, self.fs.pwd.name)

    def test_cd_to_subdir(self):
        pwd = self.fs.cd(FS_SUBDIR)
        self.assertIsInstance(pwd, FileSystemNode)
        self.assertEqual(FS_SUBDIR, pwd.name)
        self.assertIs(pwd, self.fs.pwd)

    def test_size_calc(self):
        pwd_size = self.fs.lsal()
        self.assertEqual(pwd_size, TEST_FILE_SIZE)


class testDirectory(unittest.TestCase):

    def setUp(self) -> None:
        self.d = Directory(name=FS_SUBDIR)

    def test_empty_dir_size_0(self):
        # empty dir has size 0
        self.assertEqual(0, self.d.total_size())

class TestFile(unittest.TestCase):

    def setUp(self) -> None:
        self.f = File(name=TEST_FILE_NAME, size=TEST_FILE_SIZE)

    def test_total_size(self):
        self.assertEqual(TEST_FILE_SIZE, self.f.total_size())


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
