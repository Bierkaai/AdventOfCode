import unittest

from models.counters import WrapAroundInt

WRAPAROUND = 4

INITIAL_INT_VALUE = 1


class TestWraparoundInt(unittest.TestCase):

    def setUp(self) -> None:
        self.i = WrapAroundInt(
            wraparound = WRAPAROUND,
            initial_value = INITIAL_INT_VALUE
        )

    def test_initial_value(self):
        self.assertEqual(INITIAL_INT_VALUE, self.i.value)

    def test_to_int(self):
        self.assertEqual(INITIAL_INT_VALUE, int(self.i))

    def test_increment(self):
        self.i.increment()
        self.assertEqual(INITIAL_INT_VALUE + 1, self.i.value)

    def test_add_1(self):
        result = self.i + 1
        self.assertEqual(INITIAL_INT_VALUE + 1, result)

    def test_add_wraparound(self):
        result = self.i + WRAPAROUND
        self.assertEqual(INITIAL_INT_VALUE, result)

    def test_wraparound_incrementally(self):
        for i in range(WRAPAROUND):
            self.i.increment()
        self.assertEqual(INITIAL_INT_VALUE, self.i.value)



if __name__ == '__main__':
    unittest.main()
