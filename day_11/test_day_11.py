import unittest
from unittest import TestCase

import numpy as np

from day_11 import Octopus
from day_11 import parse_input
from day_11 import Grid

SMALL_EXAMPLE_LIST_COUNT = 3
SMALL_EXAMPLE_LIST_LENGHT = 3

SMALL_EXAMPLE = """123
456
789"""

SMALL_EXAMPLE_PARSED_TO_LIST = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

SMALL_EXAMPLE_ENERGY_ADDED = [
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10]
]
SMALL_EXAMPLE_OCTOPUT_COUNT = 9

EXAMPLE_INPUT = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

EXAMPLE_STEP_1 = """6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637"""

EXAMPLE_STEP_2 = """8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848"""

EXAMPLE_STEP_100 = """0397666866
0749766918
0053976933
0004297822
0004229892
0053222877
0532222966
9322228966
7922286866
6789998766"""

FLASHCOUNT_STEP_100 = 1656


class TestOctopus(TestCase):

    def setUp(self) -> None:
        self.o = Octopus(1)

    def test_flash_count_zero_on_creation(self):
        self.assertEqual(0, self.o.flashcount)


    def test_add_neighbor(self):
        # adding a neighbor should increase neighbor_count
        # and have that neighbor in the set of neighbors
        neighbor = Octopus(2)
        self.o.add_neighbor(neighbor)
        self.assertIn(neighbor, self.o.neighbors, "Neigbor was not added")

    def test_neighbor_reciprocity(self):
        neighbor = Octopus(2)
        self.o.add_neighbor(neighbor)
        self.assertIn(self.o, neighbor.neighbors)

    def test_increase_energy(self):
        self.o.increase_energy()
        self.assertEqual(2, self.o.energy_level)


class TestOctopusFiringBehavior(unittest.TestCase):

    def setUp(self) -> None:
        self.o_hot = Octopus(10)
        self.hot_neighbor = Octopus(9)
        self.cool_neighbor = Octopus(1)
        self.o_hot.add_neighbor(self.hot_neighbor)
        self.o_hot.add_neighbor(self.cool_neighbor)

    def test_step_hot_octopus_fires_and_sets_energy_to_0(self):
        self.o_hot.step()
        self.assertEqual(self.o_hot.energy_level, 0)

    def test_step_hot_octopus_increases_flash_count(self):
        self.o_hot.step()
        self.assertEqual(1, self.o_hot.flashcount)

    def test_step_hot_octopus_increases_neighbor_energy(self):
        self.o_hot.step()
        self.assertEqual(self.hot_neighbor.energy_level, 10)
        self.assertEqual(self.cool_neighbor.energy_level, 2)

    def test_neighbor_flash_increases_energy_level(self):
        self.o_hot.neighbor_flash()
        self.assertEqual(11, self.o_hot.energy_level)

    def test_step_fired_octopus_does_not_increase_energy_again_on_incoming_flashes(self):
        self.o_hot.step()
        self.o_hot.neighbor_flash()
        self.assertEqual(self.o_hot.energy_level, 0)




class TestInputParser(TestCase):

    def setUp(self) -> None:
        self.result = parse_input(SMALL_EXAMPLE)

    def test_parse_input_yields_list_of_str(self):
        self.assertIsInstance(self.result, list)
        self.assertEqual(SMALL_EXAMPLE_LIST_COUNT, len(self.result))
        self.assertListEqual(SMALL_EXAMPLE_PARSED_TO_LIST, self.result)

    @unittest.skip
    def test_parse_input_yields_octopus_list(self):
        # parse input should return an octopus list with
        # the number of octopuses in the input linesxline length
        self.assertIsInstance(self.result, list)
        self.assertEqual(SMALL_EXAMPLE_OCTOPUT_COUNT, len(self.result))
        for i, o in enumerate(self.result):
            self.assertIsInstance(o, Octopus, f"Item {i} in result list is not an Octopus object")


class TestGrid(TestCase):

    def setUp(self) -> None:
        self.g = Grid(parse_input(SMALL_EXAMPLE))

    def test_row_length_is_set_correctly(self):
        self.assertEqual(SMALL_EXAMPLE_LIST_LENGHT, self.g.row_length)

    def test_grid_data_attribute_populated_with_lists_of_list_of_octopuses(self):
        for row in self.g.data:
            for o in row:
                self.assertIsInstance(o, Octopus)

    def test_grid_str(self):
        self.assertEqual(SMALL_EXAMPLE, str(self.g))

    def test_yield_octopuses_in_row_i_around_pos_j_top_left_case(self):
        result = [x.energy_level for x in self.g.yield_octopuses_in_row_i_around_pos_j(0,0)]
        self.assertListEqual(result, [1, 2])

    def test_yield_octopuses_in_row_i_around_pos_j_middle_case(self):
        result = [x.energy_level for x in self.g.yield_octopuses_in_row_i_around_pos_j(1,1)]
        self.assertListEqual(result, [4, 5, 6])

    def test_yield_octopuses_in_row_i_around_pos_j_bottom_case(self):
        result = [x.energy_level for x in self.g.yield_octopuses_in_row_i_around_pos_j(2,2)]
        self.assertListEqual(result, [8, 9])

    def test_get_octopus_at_i_j(self):
        result = self.g.get_octopus_at(0, 1).energy_level
        self.assertEqual(2, result)

    def test_iter_yields_all_octopuses(self):
        for o in self.g:
            self.assertIn(o.energy_level, set(range(1, 10)))

    def test_neighbors_for_octopuses_are_set(self):
        for o in self.g:
            self.assertGreater(len(o.neighbors), 0)

    def test_neighbors_set(self):
        neighbors = {o.energy_level for o in self.g.get_octopus_at(0,1).neighbors}
        self.assertSetEqual(neighbors, {1,3,4,5,6})

    def test_int_grid(self):
        self.assertListEqual(SMALL_EXAMPLE_PARSED_TO_LIST, self.g.get_int_grid())

    def test_max_energy(self):
        self.assertEqual(9, self.g.max_energy)

    def test_add_energy(self):
        self.g.add_energy()
        self.assertListEqual(SMALL_EXAMPLE_ENERGY_ADDED, self.g.get_int_grid())

class TestExampleCase(unittest.TestCase):

    def setUp(self) -> None:
        self.g = Grid(parse_input(EXAMPLE_INPUT))

    def test_first_step(self):
        self.g.do_step()
        self.assertEqual(str(self.g), EXAMPLE_STEP_1)

    def test_second_step(self):
        self.g.do_step()
        self.g.do_step()
        self.assertEqual(str(self.g), EXAMPLE_STEP_2)

class Test100Steps(unittest.TestCase):

    def setUp(self) -> None:
        self.g = Grid(parse_input(EXAMPLE_INPUT))
        for _ in range(100):
            self.g.do_step()

    def test_100_steps(self):
        self.assertEqual(str(self.g), EXAMPLE_STEP_100)

    def test_flashcount(self):
        self.assertEqual(FLASHCOUNT_STEP_100, self.g.flashcount)


