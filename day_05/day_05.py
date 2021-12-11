import re
from itertools import zip_longest

PATTERN = r"([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)"


def parse_line(l):
    matches = re.match(PATTERN, l)
    if not matches:
        return None
    return tuple([int(x) for x in matches.groups()])


def make_range(p1, p2):
    if p1 > p2:
        return range(p1, p2 - 1, -1)
    if p1 <= p1:
        return range(p1, p2 + 1)


class Line(object):

    def __init__(self, spec):
        """

        :param spec:
            tuple with 4 entries (x1, y1, x2, y2)
        """
        self.spec = spec
        self.x1, self.y1, self.x2, self.y2 = self.spec
        self.is_horizontal = self.y1 == self.y2
        self.is_vertical = self.x1 == self.x2
        self.is_diagonal = not (self.is_vertical or self.is_horizontal)

    def generate_points(self):
        if self.is_horizontal:
            for x in make_range(self.x1, self.x2):
                yield x, self.y1
        if self.is_vertical:
            for y in make_range(self.y1, self.y2):
                yield self.x1, y
        if self.is_diagonal:
            yield from zip(
                make_range(self.x1, self.x2),
                make_range(self.y1, self.y2)
            )


class OverlapCounter(object):

    def __init__(self):
        self.known_points = set()
        self.overlapping_points = set()

    def add(self, p):
        if p in self.known_points:
            self.overlapping_points.add(p)
        else:
            self.known_points.add(p)

    @property
    def count(self):
        return len(self.overlapping_points)


def solve(input_lines):
    oc = OverlapCounter()
    oc2 = OverlapCounter()
    for line in input_lines:
        tup = parse_line(line)
        if tup is not None:
            l = Line(tup)
            for point in l.generate_points():
                if not l.is_diagonal:
                    oc.add(point)
                oc2.add(point)
    return oc.count, oc2.count


if __name__ == "__main__":
    oc = OverlapCounter()
    oc2 = OverlapCounter()

    with open("../input/05.txt", 'r') as f_obj:
        for line in f_obj:
            tup = parse_line(line)
            if tup is not None:
                l = Line(tup)
                for point in l.generate_points():
                    if not l.is_diagonal:
                        oc.add(point)
                    oc2.add(point)

    print(f"Case 1: {oc.count})")
    print(f"Case 2: {oc2.count}")
