import unittest

from day_21 import Game

TEST_CASE_PLAYERS = [4, 8]

FIRST_DIE_ROLL = 6
SECOND_DIE_ROLL = 15

PLAYER_1_POSITION_AFTER_1_MOVE = 10
PLAYER_2_POSITION_AFTER_1_MOVE = 3
PLAYER_1_POSITION_AFTER_2_MOVES = 4
PLAYER_2_POSITION_AFTER_2_MOVES = 6

PLAYER_1_SCORE_AFTER_2_MOVES = 14
PLAYER_2_SCORE_AFTER_2_MOVES = 9


class TestGame(unittest.TestCase):

    def setUp(self) -> None:
        self.g = Game(TEST_CASE_PLAYERS)

    def test_die_roll_1_2(self):
        self.assertEqual(FIRST_DIE_ROLL, self.g.roll_die())
        self.assertEqual(3, self.g.die_roll_count)
        self.assertEqual(SECOND_DIE_ROLL, self.g.roll_die())
        self.assertEqual(6, self.g.die_roll_count)

    def test_player_position_after_first_move(self):
        self.g.move_players()
        self.assertEqual(PLAYER_1_POSITION_AFTER_1_MOVE, int(self.g.players[0]))
        self.assertEqual(PLAYER_2_POSITION_AFTER_1_MOVE, int(self.g.players[1]))




if __name__ == '__main__':
    unittest.main()
