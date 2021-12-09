import collections.abc

from unittest import TestCase

from day_09 import GridBuilder

EXAMPLE_INPUT = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678"
]

EXAMPLE_LINE_1_LOWS = [1, 0]

EXAMPLE_OUTPUT = 15

READABLE_LINES = [f"{i}" * 10 for i in range(10)]

READABLE_INDEX = list(range(10))


class TestGBLineBuffer(TestCase):

    def setUp(self) -> None:
        self.gb = GridBuilder()

    def test_add_one_line(self):
        self.gb.add_line(READABLE_LINES[0])
        self.assertEqual(READABLE_LINES[0], self.gb.linebuffer[2])

    def test_two_lines(self):
        self.gb.add_line(READABLE_LINES[0])
        self.gb.add_line(READABLE_LINES[1])
        self.assertEqual(READABLE_LINES[1], self.gb.linebuffer[2])

    def test_cycle(self):
        self.gb.add_line(READABLE_LINES[0])
        self.gb.add_line(READABLE_LINES[1])
        self.gb.add_line(READABLE_LINES[2])
        self.gb.add_line(READABLE_LINES[3])
        self.assertEqual(READABLE_LINES[3], self.gb.linebuffer[2])
        self.assertEqual(READABLE_LINES[2], self.gb.linebuffer[1])
        self.assertEqual(READABLE_LINES[1], self.gb.linebuffer[0])
        self.gb.add_line(READABLE_LINES[4])
        self.assertEqual(READABLE_LINES[3], self.gb.linebuffer[1])


class TestGBFindLows(TestCase):
    # as soon as a line is added and linebuffer[1] is not empty
    # a list of minimums should be emitted
    def setUp(self) -> None:
        self.gb = GridBuilder()
        self.results = []
        self.results = [self.gb.add_line(l) for l in EXAMPLE_INPUT]

    def test_add_line_returns_iterable(self):
        for r in self.results:
            self.assertIsInstance(r, collections.abc.Iterable, "GridBuilder.add_line does not always return iterable")

    def test_adding_line_1_emits_empty_list(self):
        self.assertEqual([], self.results[0])

    def test_adding_line_2_emits_non_empty_list(self):
        self.assertGreater(len(self.results[1]), 0)

    def test_adding_line_2_emits_low_points_in_line_1(self):
        self.assertListEqual(EXAMPLE_LINE_1_LOWS, self.results[1])


class TestGBSlice(TestCase):

    def setUp(self) -> None:
        self.gb = GridBuilder()
        self.gb.add_line(READABLE_INDEX)

    def test_get_empty_list_from_linebuffer_slice(self):
        # trying to get a slice from non-existent line buffer entry yields empty list
        result = self.gb.get_linebuffer_slice(buffer_id=1, start=0, end=1)
        self.assertEqual([], result)

    def test_get_subzero_slice_returns_positive(self):
        result = self.gb.get_linebuffer_slice(buffer_id=2, start=-1, end=2)
        self.assertEqual([0, 1], result)

    def test_get_after_len_returns_last_part(self):
        result = self.gb.get_linebuffer_slice(buffer_id=2, start=8, end=12)
        self.assertEqual([8, 9], result)


class TestGBNeighborhood(TestCase):

    def setUp(self) -> None:
        self.gb = GridBuilder()
        self.gb.add_line(READABLE_LINES[0])

    def test_get_neighborhood_zero_case(self):
        expected = {0}
        self.assertSetEqual(expected, self.gb.get_neighborhood(0))

    def test_get_neighborhood_regular_case(self):
        self.gb.add_line(READABLE_LINES[1])
        self.gb.add_line(READABLE_LINES[2])
        expected = {0, 1, 2}
        self.assertSetEqual(expected, self.gb.get_neighborhood(2))
