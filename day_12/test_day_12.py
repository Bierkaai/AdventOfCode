import unittest

from unittest import TestCase

from day_12 import CaveNetwork

START_CAVE_LABEL = "start"

STUPID_EXAMPLE = """start-A
A-end"""

SIMPLE_EXAMPLE = """start-A
A-b
b-end
A-end"""

SIMPLE_EXAMPLE_LIST = [
    "start-A",
    "A-b",
    "b-end",
    "A-end"
]

SIMPLE_EXAMPLE_EDGE_LIST = [("start", "A"),
                            ("A", "b"),
                            ("b", "end"),
                            ("A", "end")]

NODES_IN_SIMPLE_EXAMPLE = 4
N_PATHS_IN_SIMPLE_EXAMPLE = 3
SMALL_CAVES_IN_SIMPLE_EXAMPLE = {'start', 'b', 'end'}

ALL_PATHS_IN_SIMPLE_EXAMPLE = {
    ("start", "A", "end"),
    ("start", "A", "b", "end"),
    ("start", "A", "b", "A", "end")
}

ALL_PATHS_IN_SIMPLE_EXAMPLE_WITH_REVISIT = {
    ("start", "A", "end"),
    ("start", "A", "b", "end"),
    ("start", "A", "b", "A", "b", "end"),
    ("start", "A", "b", "A", "b", "A", "end")
}

EXAMPLE_INPUT = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

ALL_PATHS_IN_EXAMPLE = {
    ("start", "A", "b", "A", "c", "A", "end"),
    ("start", "A", "b", "A", "end"),
    ("start", "A", "b", "end"),
    ("start", "A", "c", "A", "b", "A", "end"),
    ("start", "A", "c", "A", "b", "end"),
    ("start", "A", "c", "A", "end"),
    ("start", "A", "end"),
    ("start", "b", "A", "c", "A", "end"),
    ("start", "b", "A", "end"),
    ("start", "b", "end")
}
N_PATHS_IN_EXAMPLE = 10

LARGER_EXAMPLE = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
N_PATHS_IN_LARGER_EXAMPLE = 19
N_PATHS_V2_IN_LARGER_EXAMPLE = 103

EVEN_LARGER_EXAMPLE = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""
N_PATHS_IN_EVEN_LARGER_EXAMPLE = 226
N_PATHS_V2_IN_EVEN_LARGER_EXAMPLE = 3509


class TestCaveNetworkBasicFunctionalityStrInput(TestCase):

    def setUp(self):
        self.cn = CaveNetwork(SIMPLE_EXAMPLE)

    def test_edge_list_is_correctly_parsed(self):
        self.assertListEqual(SIMPLE_EXAMPLE_EDGE_LIST, self.cn.edge_list)

    def test_string_is_parsed_and_correct_n_of_nodes_is_created(self):
        n_caves_in_result = self.cn.n_caves
        self.assertEqual(NODES_IN_SIMPLE_EXAMPLE, n_caves_in_result)

    def test_small_caves_list_is_made_correctly(self):
        self.assertSetEqual(SMALL_CAVES_IN_SIMPLE_EXAMPLE, self.cn.small_caves)

    def test_find_paths_simple_example(self):
        self.assertSetEqual(ALL_PATHS_IN_SIMPLE_EXAMPLE, self.cn.find_paths())

    def test_find_paths_simple_example_revisit(self):
        self.assertSetEqual(ALL_PATHS_IN_SIMPLE_EXAMPLE_WITH_REVISIT, self.cn.find_paths(revisit_one_small_cave=True))


class TestCaveNetworkBasicFunctionalityListInput(TestCase):

    def setUp(self):
        self.cn = CaveNetwork(SIMPLE_EXAMPLE_LIST)

    def test_edge_list_is_correctly_parsed(self):
        self.assertListEqual(SIMPLE_EXAMPLE_EDGE_LIST, self.cn.edge_list)

    def test_string_is_parsed_and_correct_n_of_nodes_is_created(self):
        n_caves_in_result = self.cn.n_caves
        self.assertEqual(NODES_IN_SIMPLE_EXAMPLE, n_caves_in_result)

    def test_small_caves_list_is_made_correctly(self):
        self.assertSetEqual(SMALL_CAVES_IN_SIMPLE_EXAMPLE, self.cn.small_caves)




class TestCaveNetworkPathFinding(TestCase):

    def setUp(self):
        self.cn = CaveNetwork(STUPID_EXAMPLE)

    def test_start_is_end_returns_path_with_one_node(self):
        self.assertSetEqual(self.cn.find_paths(start_cave="end"), {('end',)})

    def test_find_single_path_a_end(self):
        self.assertSetEqual(self.cn.find_paths(start_cave="start"), {('start', 'A', 'end')})


class TestExample(TestCase):

    def setUp(self) -> None:
        self.cn = CaveNetwork(EXAMPLE_INPUT)

    def test_find_all_paths_in_example(self):
        self.assertSetEqual(self.cn.find_paths(start_cave="start"), ALL_PATHS_IN_EXAMPLE)

    def test_count_paths_in_example(self):
        self.assertEqual(N_PATHS_IN_EXAMPLE, self.cn.count_paths())

class TestLargerExample(TestCase):

    def setUp(self) -> None:
        self.cn = CaveNetwork(LARGER_EXAMPLE)

    def test_count_paths_in_example(self):
        self.assertEqual(N_PATHS_IN_LARGER_EXAMPLE, self.cn.count_paths())

    @unittest.skip
    def test_count2_paths_in_larger_example(self):
        self.assertEqual(N_PATHS_V2_IN_LARGER_EXAMPLE, self.cn.count_paths_v2())



class TestEvenLargerExample(TestCase):

    def setUp(self) -> None:
        self.cn = CaveNetwork(EVEN_LARGER_EXAMPLE)

    def test_count_paths_in_example(self):
        self.assertEqual(N_PATHS_IN_EVEN_LARGER_EXAMPLE, self.cn.count_paths())