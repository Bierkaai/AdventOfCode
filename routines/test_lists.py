import types
from unittest import TestCase

from lists import generate_sublists

TEST_LIST = [
    "a", 1, 2, 3, "b", 1, 2, 3
]

SUBLIST_2_RESULT = [
    ("a", 1),
    (2, 3),
    ("b", 1),
    (2, 3)
]

SUBLIST_5_RESULT = [
    ("a", 1, 2, 3, "b"),
    (1, 2, 3, None, None)
]

SUBLIST_5_RESULT_TRUNCATE = [
    ("a", 1, 2, 3, "b"),
    (1, 2, 3)
]



class Testsublister(TestCase):

    def test_generate_sublists_2(self):
        result = generate_sublists(TEST_LIST, 2)
        self.assertIsInstance(result, types.GeneratorType)
        self.assertListEqual(SUBLIST_2_RESULT, list(result))

    def test_generate_sublists_5(self):
        result = generate_sublists(TEST_LIST, 5)
        self.assertIsInstance(result, types.GeneratorType)
        self.assertListEqual(SUBLIST_5_RESULT, list(result))

    def test_generate_sublists_truncate(self):
        result = generate_sublists(TEST_LIST, 5, truncate=True)
        self.assertIsInstance(result, types.GeneratorType)
        self.assertListEqual(SUBLIST_5_RESULT_TRUNCATE, list(result))