import unittest

from aocd.models import Puzzle

from y2023.day01 import solve_a, solve_b, find_all_numbers, create_digit_list, create_number

ONE_DIGIT_EX = "treb7uchet"
ONE_DIGIT_EX_STR_LIST = ["7"]
ONE_DIGIT_EX_EXPECTED_LIST = [7, 7]
ONE_DIGIT_EX_EXPECTED_NR = 77


LETTER_DIGIT_EX = "two1nineeight4wo"
LETTER_DIGIT_EX_STR_LIST_NO_WORDS = ["1", "4"]
LETTER_DIGIT_EX_STR_LIST = ["two", "1", "nine", "eight", "4"]

LETTER_DIGIT_EXTRACT_EXPECTED = [2, 1, 9, 8, 4]

LETTER_DIGIT_EX_EXPECTED_LIST = [2, 4]
LETTER_DIGIT_EX_EXPECTED_NR = 24

EXAMPLE_B_DATA = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

YEAR = 2023
DAY = 1
EXAMPLE_RESULT_A = 142
EXAMPLE_RESULT_B = 281

puzzle = Puzzle(year=YEAR, day=DAY)
EXAMPLE_DATA = puzzle.example_data


class TestHelperFunctions(unittest.TestCase):
    def test_extract_list_one_number(self):
        response = find_all_numbers(ONE_DIGIT_EX)
        self.assertListEqual(response, ONE_DIGIT_EX_STR_LIST)

    def test_extract_list_more_numbers(self):
        response = find_all_numbers(LETTER_DIGIT_EX, allow_written=False)
        self.assertListEqual(response, LETTER_DIGIT_EX_STR_LIST_NO_WORDS)

    def test_extract_list_more_numbers_written_digits(self):
        response = find_all_numbers(LETTER_DIGIT_EX, allow_written=True)
        self.assertListEqual(response, LETTER_DIGIT_EX_STR_LIST)

    def test_extract_digits(self):
        response = create_digit_list(LETTER_DIGIT_EX_STR_LIST)
        self.assertListEqual(response, LETTER_DIGIT_EXTRACT_EXPECTED)

    def test_make_number(self):
        response = create_number(LETTER_DIGIT_EXTRACT_EXPECTED)
        self.assertEqual(response, LETTER_DIGIT_EX_EXPECTED_NR)


class TestDay01(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.example_data = EXAMPLE_DATA
        cls.example_result_a = EXAMPLE_RESULT_A
        cls.example_result_b = EXAMPLE_RESULT_B

    def test_example_a(self):
        result = solve_a(self.example_data)
        self.assertEqual(self.example_result_a, result,
                         f"Example result should be {self.example_result_a}, not {result}")

    def test_example_b(self):
        result = solve_b(EXAMPLE_B_DATA)
        self.assertEqual(self.example_result_b, result,
                         f"Example result B should be {self.example_result_b}, not {result}")


if __name__ == '__main__':
    unittest.main()
