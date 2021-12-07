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

    @property
    def hasWon(self):
        return set() in self._rows or set() in self._cols

    def mark(self, nr):
        nr_as_set = {nr}
        self._rows = [r - nr_as_set for r in self._rows]
        self._cols = [c - nr_as_set for c in self._cols]
