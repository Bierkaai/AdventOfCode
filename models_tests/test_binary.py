from unittest import TestCase

from models.binary import Bits

BITLENGTH = 5

EXAMPLE_BITSTRING = "10011"
EXAMPLE_INT = 19
EXAMPLE_BITCOUNT = 3
EXAMPLE_MOST_COMMON_BIT = 1
EXAMPLE_INVERSION = "01100"
EXAMPLE_INVERSION_INT = 12

OTHER_BITSTRING = "10010"
OTHER_INT = 18

class TestBits(TestCase):

    def setUp(self):
        self.bit = Bits(bit_str=EXAMPLE_BITSTRING, length=BITLENGTH)

    def test_len(self):
        self.assertEqual(BITLENGTH, len(self.bit))

    def test_get_str(self):
        self.assertEqual(EXAMPLE_BITSTRING, str(self.bit))

    def test_get_int_value(self):
        self.assertEqual(EXAMPLE_INT, int(self.bit))

    def test_bit_count(self):
        self.assertEqual(EXAMPLE_BITCOUNT, self.bit.bit_count)

    def test_most_common_bit(self):
        self.assertEqual(EXAMPLE_MOST_COMMON_BIT, self.bit.most_common_bit)

    def test_inversion(self):
        inverted = ~self.bit
        self.assertEqual(BITLENGTH, len(inverted), "Incorrect length in inversion")
        self.assertEqual(EXAMPLE_INVERSION, str(inverted), "String value of inversion incorrect")
        self.assertEqual(EXAMPLE_INVERSION_INT, int(inverted), "Int value of inversion incorrect")
