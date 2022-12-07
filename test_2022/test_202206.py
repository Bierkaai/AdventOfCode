import unittest

from aocd.models import Puzzle

from y2022.day03 import solve_a, solve_b

YEAR = 2022
DAY = 6
EXAMPLE_RESULT_A = 95437
EXAMPLE_RESULT_B = None

#puzzle = Puzzle(year=YEAR, day=DAY)
#EXAMPLE_DATA = puzzle.example_data

EXAMPLE_DATA = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

class TestFileSystem(unittest.TestCase):

    def test_fs(self):
        pass

@unittest.skip
class TestDay06(unittest.TestCase):

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
