from typing import Tuple, List

from aocd.models import Puzzle

DAY = 5
YEAR = 2022


def parse_and_split_input(raw_input: str) -> Tuple[List[str], List[str]]:
    dock = []
    moves = []
    doing_dock = True
    for line in raw_input.splitlines(keepends=False):
        if doing_dock and len(line) > 0:
            dock.append(line)
        elif len(line) == 0:
            doing_dock = False
        else:
            moves.append(line)
    return dock, moves


def parse_move_instruction(move_str: str) -> Tuple[int, int, int]:
    tokenized = move_str.split()
    return tuple(int(tokenized[x]) for x in (1, 3, 5))


class DockCrane:

    def __init__(self, dockdesc: List[str]):
        self.dock_nrs = dockdesc[-1]
        self.dock = dict()
        docklines = dockdesc[:-1]
        for pos, nr in enumerate(self.dock_nrs):
            try:
                self.dock[int(nr)] = [line[pos] for line in docklines if line[pos] != " "]
            except ValueError:
                continue

    def read_topline(self):
        return "".join([x[0] for x in self.dock.values()])

    def move(self, n, source, target):
        for _ in range(n):
            self.dock[target].insert(0, self.dock[source].pop(0))

    def move_from_str(self, move_str):
        self.move(*parse_move_instruction(move_str))


class DockCrane9001(DockCrane):

    def move(self, n, source, target):
        self.dock[target] = self.dock[source][:n] + self.dock[target]
        del self.dock[source][:n]


def solve_a(data):
    dock, moves = parse_and_split_input(data)
    d = DockCrane(dock)
    for move_str in moves:
        d.move_from_str(move_str)
    return d.read_topline()


def solve_b(data):
    dock, moves = parse_and_split_input(data)
    d = DockCrane9001(dock)
    for move_str in moves:
        d.move_from_str(move_str)
    return d.read_topline()


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
