from unittest import TestCase

from day_05.day_05 import parse_line, Line, make_range, OverlapCounter, solve

SEXOND_EXAMPLE_ANSWER = 12

EXAMPLE_INPUT = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

EXAMPLE_ANSWER = 5

FIRST_LINE = "0,9 -> 5,9"
FIRST_LINE_PARSED_TUPLE = (0, 9, 5, 9)

SECOND_LINE = "8,0 -> 0,8"
SECOND_LINE_PARSED_TUPLE = (8, 0, 0, 8)

REAL_INPUT_LINE = "233,182 -> 233,295"
REAL_INPUT_LINE_PARSED_TUPLE = (233, 182, 233, 295)

VLINE = (48, 2, 48, 4)

VLINE_POINTS = [
    (48, 2),
    (48, 3),
    (48, 4)
]

HORIZONTAL_LINE_REVERSED = (48, 4, 48, 2)
HLINE_REV_POINTS = [
    (48, 4),
    (48, 3),
    (48, 2)
]

HLINE = (12, 10, 15, 10)
HLINE_POINTS = [
    (12, 10),
    (13, 10),
    (14, 10),
    (15, 10)
]
DIAGONAL_LINE = (6, 4, 2, 0)
DLINE_POINTS = [
    (6, 4),
    (5, 3),
    (4, 2),
    (3, 1),
    (2, 0)
]

DIAGONAL_LINE_2 = (5, 5, 8, 2)
DLINE_POINTS_2 = [
    (5, 5),
    (6, 4),
    (7, 3),
    (8, 2)
]

A_POINT = (1, 4)
ANOTHER_POINT = (2, 5)


class TestLine(TestCase):

    def test_first_line(self):
        response = parse_line(FIRST_LINE)
        self.assertEquals(FIRST_LINE_PARSED_TUPLE, response)

    def test_second_line(self):
        response = parse_line(SECOND_LINE)
        self.assertEqual(SECOND_LINE_PARSED_TUPLE, response)

    def test_real_input(self):
        response = parse_line(REAL_INPUT_LINE)
        self.assertEqual(REAL_INPUT_LINE_PARSED_TUPLE, response)

    def test_empty_line(self):
        response = parse_line("")
        self.assertIsNone(response)


class TestHorizontalLine(TestCase):

    def setUp(self) -> None:
        self.line = Line(HLINE)
        self.revline = Line(HORIZONTAL_LINE_REVERSED)

    def test_get_points(self):
        self.assertListEqual(HLINE_POINTS, list(self.line.generate_points()))

    def test_get_points_reversed(self):
        self.assertListEqual(HLINE_REV_POINTS, list(self.revline.generate_points()))


class TestVerticalLine(TestCase):

    def setUp(self) -> None:
        self.line = Line(HLINE)

    def test_get_points(self):
        self.assertListEqual(HLINE_POINTS, list(self.line.generate_points()))


class TestDiagonalLine(TestCase):
    def setUp(self) -> None:
        self.line = Line(DIAGONAL_LINE)

    def test_get_points(self):
        self.assertListEqual(DLINE_POINTS, list(self.line.generate_points()))


class TestDiagonalLine2(TestCase):
    def setUp(self) -> None:
        self.line = Line(DIAGONAL_LINE_2)

    def test_get_points(self):
        self.assertListEqual(DLINE_POINTS_2, list(self.line.generate_points()))


class TestLineProperties(TestCase):

    def setUp(self) -> None:
        self.hl = Line(HLINE)
        self.vl = Line(VLINE)
        self.dl = Line(DIAGONAL_LINE)

    def test_is_horizontal(self):
        self.assertTrue(self.hl.is_horizontal, "Horizontal line's is_horizontal attr should be true")
        self.assertFalse(self.vl.is_horizontal, "Vertical line's is_horizontal attr should be false")
        self.assertFalse(self.dl.is_horizontal, "Diagonal line's is_horizontal attr should be false")

    def test_is_vertical(self):
        self.assertTrue(self.vl.is_vertical, "Vertical line's is_vertical attr should be true")
        self.assertFalse(self.hl.is_vertical, "Horizontal line's is_vertical attr should be false")
        self.assertFalse(self.dl.is_vertical, "Diagonal line's is_vertical attr should be false")

    def test_is_diagonal(self):
        self.assertFalse(self.vl.is_diagonal, "Vertical line's is_diagonal attr should be false")
        self.assertFalse(self.hl.is_diagonal, "Horizontal line's is_diagonal attr should be false")
        self.assertTrue(self.dl.is_diagonal, "Diagonal line's is_diagonal attr should be true")


class TestRangeMaker(TestCase):

    def test_make_range(self):
        self.assertEquals(range(1, 4), make_range(1, 3))

    def test_make_reversed_range(self):
        self.assertEquals(range(3, 0, -1), make_range(3, 1))

    def test_listed_revers(self):
        self.assertListEqual([3, 2, 1], list(make_range(3, 1)))

    def test_make_range_len_1(self):
        self.assertEquals(range(1, 2), make_range(1, 1))


class TestOverlapCounter(TestCase):

    def setUp(self) -> None:
        self.oc = OverlapCounter()

    def test_add_point(self):
        self.oc.add(A_POINT)
        self.assertEqual(0, self.oc.count, "Adding a single point should not cause overlapcounter to increase")

    def test_add_point_twice(self):
        self.oc.add(A_POINT)
        self.oc.add(A_POINT)
        self.assertEqual(1, self.oc.count, "Adding a single point twice should cause overlapcounter to be 1")

    def test_add_point_three_times(self):
        self.oc.add(A_POINT)
        self.oc.add(A_POINT)
        self.oc.add(A_POINT)
        self.assertEqual(1, self.oc.count, "Adding a single point thrice should cause overlapcounter to still be 1")

    def test_non_overlapping_points(self):
        self.oc.add(A_POINT)
        self.oc.add(ANOTHER_POINT)
        self.assertEqual(0, self.oc.count, "Adding non-overlapping points should not cause overlapcounter to increase")


class TestExampleCase(TestCase):

    def setUp(self) -> None:
        self.example_lines = EXAMPLE_INPUT.split("\n")

    def test_example_answer(self):
        self.assertEqual(EXAMPLE_ANSWER, solve(self.example_lines)[0])

    def test_second_example(self):
        self.assertEqual(SEXOND_EXAMPLE_ANSWER, solve(self.example_lines)[1])
