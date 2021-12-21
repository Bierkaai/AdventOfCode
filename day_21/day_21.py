from models.counters import WrapAroundInt

DIE_ROLLS = 3

DIE_INITIAL_VALUE = 0
DIE_MAX_VALUE = 100
PLAYER_1_START = 7
PLAYER_2_START = 6


class Game(object):

    def __init__(self, players):
        self.die = WrapAroundInt(wraparound=DIE_MAX_VALUE, initial_value=DIE_INITIAL_VALUE)
        self.players = players
        self.die_roll_count = 0

    def roll_die(self):
        self.die_roll_count += DIE_ROLLS
        return sum([self.die.increment() for _ in range(DIE_ROLLS)])


if __name__ == "__main__":
    players = [PLAYER_1_START, PLAYER_2_START]
    game = Game(players)
