import types
import unittest

from aocd.models import Puzzle

from y2022.day03 import solve_a, solve_b
from y2022.day03 import Rucksack, calculate_priority, split_in_groups, split_lines, find_common_item

YEAR = 2022
DAY = 3
EXAMPLE_RESULT_A = 157
EXAMPLE_RESULT_B = 70

puzzle = Puzzle(year=YEAR, day=DAY)
EXAMPLE_DATA = puzzle.example_data

EXAMPLE_RUCKSACK = "vJrwpWtwJgWrhcsFMMfFFhFp"
EXAMPLE_COMP_1 = "vJrwpWtwJgWr"
EXAMPLE_COMP_2 = "hcsFMMfFFhFp"
EXAMPLE_ITEMCOUNT = 24
EXAMPLE_ITEMS_PER_COMP = 12
EXAMPLE_COMMON_ITEM = "p"

EXAMPLE_PRIORITIES = (
    ('p', 16),
    ('L', 38),
    ('P', 42),
    ('v', 22)
)

EXAMPLE_STRING = """AAA
BBB
CCC
DDD
EEE
FFF
GGG
"""

EXAMPLE_SPLITLINES = [
    "AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG"
]

EXAMPLE_GROUPS_4 = [
    ("AAA", "BBB", "CCC", "DDD"),
    ("EEE", "FFF", "GGG")
]

EXAMPLE_GROUPS_3 = [
    ("AAA", "BBB", "CCC"),
    ("DDD", "EEE", "FFF"),
    ("GGG",)
]

EXAMPLE_GROUP_PARSED = [
    ("vJrwpWtwJgWrhcsFMMfFFhFp",
     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
     "PmmdzqPrVvPwwTWBwg"),
    ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
     "ttgJtRGJQctTZtZT",
     "CrZsJsPPZsGzwwsLwLmpwMDw",)
]

FIRST_GROUP_COMMON_ITEM = 'r'
SECOND_GROUP_COMMON_ITEM = 'Z'


class TestRucksack(unittest.TestCase):

    def setUp(self) -> None:
        self.r = Rucksack(EXAMPLE_RUCKSACK)

    def test_itemcount(self):
        self.assertEqual(EXAMPLE_ITEMCOUNT, self.r.itemcount)

    def test_items_per_compartment(self):
        self.assertEqual(EXAMPLE_ITEMS_PER_COMP, self.r.items_per_compartment)

    def test_split_compartments(self):
        self.assertEqual(EXAMPLE_COMP_1, self.r.compartments[0])
        self.assertEqual(EXAMPLE_COMP_2, self.r.compartments[1])

    def test_find_common_item(self):
        self.assertEqual(EXAMPLE_COMMON_ITEM, self.r.find_common_item_in_all_compartments())


class TestComputePriority(unittest.TestCase):

    def test_prio_p(self):
        for i, case in enumerate(EXAMPLE_PRIORITIES):
            with self.subTest(i=i):
                c, prio = case
                self.assertEqual(prio, calculate_priority(c))


class TestGroupRucksacks(unittest.TestCase):

    def test_splitlines(self):
        result = split_lines(EXAMPLE_STRING)
        self.assertIsInstance(result, types.GeneratorType)
        self.assertListEqual(EXAMPLE_SPLITLINES, list(result))

    def test_split_in_groups_3(self):
        result = split_in_groups(EXAMPLE_SPLITLINES, 3)
        self.assertIsInstance(result, types.GeneratorType)
        self.assertListEqual(EXAMPLE_GROUPS_3, list(result))

    def test_split_in_groups_4(self):
        result = split_in_groups(EXAMPLE_SPLITLINES, 4)
        self.assertIsInstance(result, types.GeneratorType)
        self.assertListEqual(EXAMPLE_GROUPS_4, list(result))

    def test_split_example(self):
        result = list(split_in_groups(split_lines(EXAMPLE_DATA), 3))
        self.assertListEqual(EXAMPLE_GROUP_PARSED, result)

    def test_find_common_item_in_rucksacks(self):
        self.assertEqual(find_common_item(EXAMPLE_GROUP_PARSED[0]), FIRST_GROUP_COMMON_ITEM)
        self.assertEqual(find_common_item(EXAMPLE_GROUP_PARSED[1]), SECOND_GROUP_COMMON_ITEM)





class TestDay03(unittest.TestCase):

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
