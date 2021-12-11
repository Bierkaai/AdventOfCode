import sys

INPUT = """2238518614
4552388553
2562121143
2666685337
7575518784
3572534871
8411718283
7742668385
1235133231
2546165345"""

EXAMPLE_INPUT = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

class Octopus(object):

    def __init__(self, energy_level=0):
        self.energy_level = energy_level
        self.neighbors = set()
        self.flashcount = 0

    def add_neighbor(self, other, recipro=True):
        self.neighbors.add(other)
        if recipro:
            # let's make sure we do net enter endless recursion
            other.add_neighbor(self, recipro=False)

    def neighbor_flash(self):
        if self.energy_level != 0:
            self.increase_energy()

    def increase_energy(self):
        self.energy_level += 1

    def step(self):
        if self.energy_level > 9:
            self.energy_level = 0
            self.flashcount += 1
            for n in self.neighbors:
                n.neighbor_flash()

    def __str__(self):
        return str(self.energy_level)


class Grid(object):

    def __init__(self, data):
        self.row_length = len(data[0])
        self.data = [
            [Octopus(i) for i in row]
            for row in data
        ]
        self.set_neighbors()

    def __iter__(self):
        yield from [o for row in self.data for o in row]

    @property
    def max_energy(self):
        return max([max(r) for r in self.get_int_grid()])

    def get_int_grid(self):
        return [
            [o.energy_level for o in row]
            for row in self.data
        ]

    @property
    def gridsize(self):
        return len(self.data), self.row_length

    @property
    def flashcount(self):
        return sum(
            sum(o.flashcount for o in row)
            for row in self.data
        )

    def get_octopus_at(self, i, j):
        if 0 <= i < len(self.data) and 0 <= j < self.row_length:
            return self.data[i][j]
        raise IndexError(f"No octopuses at {i}, {j}. Gridsize = {self.gridsize}")

    def yield_octopuses_in_row_i_around_pos_j(self, i, j):
        if 0 <= i < len(self.data):
            yield from self.data[i][max(j - 1, 0):min(self.row_length, j + 2)]
        else:
            yield from []

    def set_neighbors(self):
        for i, row in enumerate(self.data):
            previous_octopus = None
            for j, octopus in enumerate(row):
                if previous_octopus:
                    octopus.add_neighbor(previous_octopus)
                for neighbor in self.yield_octopuses_in_row_i_around_pos_j(i - 1, j):
                    octopus.add_neighbor(neighbor)
                previous_octopus = octopus

    def __str__(self):
        return "\n".join(
            ["".join([str(n) for n in r])
             for r in self.data]
        )

    def add_energy(self):
        for o in self:
            o.increase_energy()

    def do_step(self):
        self.add_energy()
        while self.max_energy > 9:
            for octopus in [o for o in self if o.energy_level >= 9]:
                octopus.step()






def parse_input(lines):
    result = []
    for line in lines.split("\n"):
        stripped = line.strip()
        if len(stripped) > 0:
            result.append([int(x) for x in stripped])
    return result


if __name__ == "__main__":
    g = Grid(parse_input(EXAMPLE_INPUT))
    for _ in range(100):
        g.do_step()
    print("This is the grid after 100 steps")
    print(g)
    print()
    print(f"{g.flashcount} flashes after 100 steps")
    g2 = Grid(parse_input(INPUT))
    stepcount = 0
    while g2.max_energy > 0:
        stepcount += 1
        g2.do_step()
    print(f"Stepcount first flash sync = {stepcount}")
    print()
    print(f"This is the grid afte
    print(g2)
