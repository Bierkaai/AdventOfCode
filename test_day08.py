from unittest import TestCase

from day08 import NumberDisplayDeducer, count_numbers_in_outputs, NumberDisplay

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

ONE_LINE = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"
ONE_LINE_INPUT = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb"
ONE_LINE_OUTPUT = "fdgacbe cefdb cefbgd gcbe"

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

CORRECT_SIMPLE_NUMBER_MAP = {
    1: {"c", "f"},
    4: {"b", "c", "d", "f"},
    7: {"a", "c", "f"},
    8: {"a", "b", "c", "d", "e", "f", "g"},
}

correct_coding_input = " ".join([CORRECT_CODING[x] for x in range(10)]) + " | " + " ".join([CORRECT_CODING[x] for x in range(4)])
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


class TestStupidityNumberDisplay(TestCase):

    def setUp(self) -> None:
        self.nd = NumberDisplay('acf')
        self.ndrev = NumberDisplay('fca')

    def test_reversal(self):
        self.assertEqual(self.nd.bitstring, self.ndrev.bitstring)
        self.assertEqual(int(self.nd), int(self.ndrev))


class TestNumberDisplay(TestCase):
    # Assuming correct codes, test whether int rep works

    def setUp(self):
        self.one = NumberDisplay('cf')
        self.eight = NumberDisplay('abcdefg')
        self.zero = NumberDisplay('abcefg')
        self.seven = NumberDisplay('acf')

    def test_bitstring(self):
        self.assertEqual('1111111', self.eight.bitstring)
        self.assertEqual('1110111', self.zero.bitstring)

    def test_int(self):
        self.assertEqual(127, int(self.eight))

    def test_reversal(self):
        self.assertEqual(0, ~self.eight)
        self.assertEqual(8, ~self.zero)

    def test_equals(self):
        self.assertTrue(self.zero == self.zero)
        self.assertTrue(self.eight == self.eight)

    def test_or(self):
        self.assertEqual(self.one | self.seven, self.seven)

    def test_population_equals_length_of_strrep(self):
        self.assertEqual(len(self.seven), sum([int(x) for x in self.seven.bitstring]))


class TestNumberDisplayDeducer(TestCase):

    def setUp(self):
        self.ndd = NumberDisplayDeducer(correct_coding_input)
        self.simple_map = self.ndd.get_simple_number_map()
        self.one = self.simple_map[1]
        self.seven = self.simple_map[7]

    def test_deduce_simple_number_map(self):
        self.assertDictEqual(CORRECT_SIMPLE_NUMBER_MAP, self.simple_map)
        self.assertEqual(self.one, {"c", "f"})

    def test_deduce_top_segment(self):
        self.assertEqual({'a'}, self.ndd.deduce_top_segment(self.one, self.seven))
