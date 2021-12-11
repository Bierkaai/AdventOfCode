from unittest import TestCase

from day_10 import Parser

VALID_TEST_CHUNK = "()"
VALID_SMALL_NESTED_CHUNK = "[<>]"
VALID_COMPLETE_NESTED_CHUNK = "[<>({}){}[([])<>]]"

class TestParser(TestCase):

    def setUp(self) -> None:
        self.p = Parser()

    def test_read_char_invalid_raises_syntax_error(self):
        with self.assertRaises(SyntaxError):
            self.p.read_char("R")

    def read_string(self, s):
        for char in s:
            self.p.read_char(char)

    def test_read_valid_char_adds_closing_counterpart_to_top_of_stack(self):
        self.p.read_char("(")
        self.assertEqual(")", self.p.open_stack.pop())

    def test_no_problem_with_valid_chunk(self):
        self.read_string(VALID_TEST_CHUNK)
        self.assertEqual(0, len(self.p.open_stack))

    def test_no_problem_with_small_nested_chunk(self):
        self.read_string(VALID_SMALL_NESTED_CHUNK)
        self.assertEqual(0, len(self.p.open_stack))

    def test_no_problem_with_big_chunk(self):
        self.read_string(VALID_COMPLETE_NESTED_CHUNK)
        self.assertEqual(0, len(self.p.open_stack))

