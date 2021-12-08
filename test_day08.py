from unittest import TestCase

from day08 import NumberDisplayDeducer, count_numbers_in_outputs

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

