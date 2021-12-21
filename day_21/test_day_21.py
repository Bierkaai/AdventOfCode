import unittest

from day_21 import Game

TEST_CASE_PLAYERS = [4, 8]

FIRST_DIE_ROLL = 6
SECOND_DIE_ROLL = 15

class TestGame(unittest.TestCase):

    def setUp(self) -> None:
        self.g = Game(TEST_CASE_PLAYERS)

    def test_die_roll_1_2(self):
        self.assertEqual(FIRST_DIE_ROLL, self.g.roll_die())
        self.assertEqual(SECOND_DIE_ROLL, self.g.roll_die())


if __name__ == '__main__':
    unittest.main()
