import copy


def transpose(list_of_lists):
    tup_T = list(zip(*list_of_lists))
    return [list(t) for t in tup_T]


class BingoBoard(object):

    def __init__(self, board):
        self.original_board = copy.deepcopy(board)
        self._rows = [set(r) for r in board]
        self._cols = [set(c) for c in transpose(board)]

    @property
    def sum(self):
        return sum([sum(r) for r in self._rows])

    def __contains__(self, n):
        return any([n in r for r in self._rows])

    def __len__(self):
        return len(self.original_board)

    @property
    def hasWon(self):
        return any([len(x) < 1 for x in self._rows + self._cols])

    def mark(self, nr):
        nr_as_set = {nr}
        self._rows = [r - nr_as_set for r in self._rows]
        self._cols = [c - nr_as_set for c in self._cols]

    def __str__(self):
        result = ""
        for row in self.original_board:
            result += " ".join([f"{x: 2d}" for x in row]) + "\n"
        return result

