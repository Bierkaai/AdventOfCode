import unittest
from unittest import TestCase

from day_08 import NumberDisplayDeducer, count_numbers_in_outputs, sum_translated_numbers

EXAMPLE_INPUT = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

EXAMPLE_OUTPUT = 26
EXAMPLE_SUM = 61229

ONE_LINE = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"
ONE_LINE_INPUT = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb"
ONE_LINE_OUTPUT = "fdgacbe cefdb cefbgd gcbe"

ONE_LINE_RESULT = 8394

ONE_LINE_OUTPUT_PARSED = ["fdgacbe", "cefdb", "cefbgd", "gcbe"]
ONE_LINE_INPUT_PARSED = ["be", "cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd", "fecdb", "fabcd", "edb"]

CORRECT_CODING = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
}

invert_correct_coding = {v: k for k, v in CORRECT_CODING.items()}

CORRECT_SIMPLE_NUMBER_MAP = {
    1: {"c", "f"},
    4: {"b", "c", "d", "f"},
    7: {"a", "c", "f"},
    8: {"a", "b", "c", "d", "e", "f", "g"},
}

CORRECT_FULL_NUMBER_MAP = {
    1: {"c", "f"},
    2: {"a", "c", "d", "e", "g"},
    3: {"a", "c", "d", "f", "g"},
    4: {"b", "c", "d", "f"},
    5: {"a", "b", "d", "f", "g"},
    6: {'a', 'b', 'd', 'e', 'f', 'g'},
    7: {"a", "c", "f"},
    8: {"a", "b", "c", "d", "e", "f", "g"},
    9: {"a", "b", "c", "d", "f", "g"},
    0: {"a", "b", "c", "e", "f", "g"}
}

correct_coding_input = " ".join([CORRECT_CODING[x] for x in range(10)]) + " | " + " ".join(
    [CORRECT_CODING[x] for x in range(4)])
CORRECT_CODING_OUTPUT_SUM = 0 + 1 + 2 + 3


class TestNumberDisplayDeducer(TestCase):

    def setUp(self) -> None:
        self.ndd = NumberDisplayDeducer(ONE_LINE)

    def test_split_input_output(self):
        self.assertEqual(ONE_LINE_INPUT, self.ndd.inputstr)
        self.assertEqual(ONE_LINE_OUTPUT, self.ndd.outputstr)

    def test_make_list_of_input_and_output(self):
        # Given a string, makes a list of strings describing individual numbers
        # inputlist and outputlist should contain these outputs
        self.assertListEqual(ONE_LINE_OUTPUT_PARSED, self.ndd.outputlist)
        self.assertListEqual(ONE_LINE_INPUT_PARSED, self.ndd.inputlist)

    def count_number_in_output_of_x_should_be_y(self, x, y):
        self.assertEqual(y, self.ndd.count_in_output(x), f"Count of {x} should be {y}")

    def test_count_1_in_output_should_be_0(self):
        self.count_number_in_output_of_x_should_be_y(x=1, y=0)

    def test_count_4_in_output_should_be_1(self):
        self.count_number_in_output_of_x_should_be_y(x=4, y=1)

    def test_count_7_in_output_should_be_0(self):
        self.count_number_in_output_of_x_should_be_y(x=7, y=0)

    def test_count_8_in_output_should_be_0(self):
        self.count_number_in_output_of_x_should_be_y(x=8, y=1)


class TestExampleCase1(TestCase):

    def test_solve_example_number_count(self):
        self.assertEqual(EXAMPLE_OUTPUT, count_numbers_in_outputs(EXAMPLE_INPUT.split("\n")))


class TestNumberDisplayDeducerDeduction(TestCase):

    def setUp(self):
        self.ndd = NumberDisplayDeducer(correct_coding_input)
        self.simple_map = self.ndd.get_simple_number_map()

    def test_deduce_simple_number_map(self):
        self.assertDictEqual(CORRECT_SIMPLE_NUMBER_MAP, self.simple_map)
        self.assertEqual(CORRECT_SIMPLE_NUMBER_MAP[1], {"c", "f"})

    def test_find_other_numbers(self):
        for n, setrep in CORRECT_FULL_NUMBER_MAP.items():
            self.assertIn(n, self.ndd.nmap, f"No representation for {n} found in nmap")
            self.assertSetEqual(self.ndd.nmap[n], setrep, f"{n} representation not correctly found")

    def test_inverted_map(self):
        for k, v in self.ndd.inverted_number_map.items():
            self.assertIsInstance(k, str)
            self.assertIsInstance(v, int)
        self.assertDictEqual(invert_correct_coding, self.ndd.inverted_number_map)


class TestNumberDeducerOutputTranslator(unittest.TestCase):

    def setUp(self) -> None:
        self.ndd = NumberDisplayDeducer(ONE_LINE)

    def test_inverted_number_map(self):
        self.assertEqual(self.ndd.inverted_number_map["be"], 1)
        self.assertEqual(self.ndd.inverted_number_map["bcdef"], 3)

    def test_output_number(self):
        self.assertEqual(ONE_LINE_RESULT, self.ndd.get_output_number())


class TestNumberTranslation(TestCase):

    def test_sum_translated_numbers(self):
        sum_result = sum_translated_numbers(EXAMPLE_INPUT.split("\n"))
        self.assertEqual(EXAMPLE_SUM, sum_result)
