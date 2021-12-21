import unittest

WRAPAROUND = 4

INITIAL_INT_VALUE = 1


class TestWraparoundInt(unittest.TestCase):

    def setUp(self) -> None:
        self.i = TestWraparoundInt(
            wraparound = WRAPAROUND,
            iniial_value = INITIAL_INT_VALUE
        )

    def test_initial_value(self):
        self.assertEqual(INITIAL_INT_VALUE, self.i.value)

    def test_to_int(self):
        self.assertEqual(INITIAL_INT_VALUE, int(self.i))

    def test_increment(self):
        self.i.increment()
        self.assertEqual(INITIAL_INT_VALUE + 1, self.i.value)

    def test_add_1(self):
        self.i += 1
        self.assertEqual(INITIAL_INT_VALUE + 1, self.i.value)

    def test_wraparound_incrementally(self):
        for i in range(WRAPAROUND):
            self.i.increment()
        self.assertEqual(INITIAL_INT_VALUE, self.i.value)



if __name__ == '__main__':
    unittest.main()
