from aocd.models import Puzzle
from string import ascii_letters
from routines.lists import generate_sublists

DAY = 3
YEAR = 2022

prio_map = {
    letter: i + 1
    for i, letter in enumerate(ascii_letters)
}


class Rucksack:

    def __init__(self, packstr, n_comp=2):
        self.packstr = packstr
        self.itemcount = len(packstr)
        self.n_comp = n_comp
        self.items_per_compartment = int(len(self.packstr) / self.n_comp)
        self.compartments = {}
        self.recompute_compartments()

    def recompute_compartments(self):
        for i in range(self.n_comp):
            self.compartments[i] = self.packstr[
                                   i * self.items_per_compartment
                                   :(i + 1) * self.items_per_compartment
                                   ]

    def find_common_item_in_all_compartments(self):
        return set.intersection(*[set(v) for v in self.compartments.values()]).pop()


def calculate_priority(character):
    return prio_map[character]


def split_lines(data):
    for line in data.splitlines(keepends=False):
        yield line


def initiate_rucksacks(data):
    return [Rucksack(s) for s in split_lines(data)]


def split_in_groups(lines, items_per_group):
    return generate_sublists(lines, items_per_group, truncate=True)


def find_common_item(rucksacks):
    return set.intersection(*[set(r) for r in rucksacks]).pop()


def solve_a(data):
    rucksacks = initiate_rucksacks(data)
    return sum([
        calculate_priority(r.find_common_item_in_all_compartments())
        for r in rucksacks
    ])


def solve_b(data):
    rucksack_teams = split_in_groups(split_lines(data), 3)
    return sum([
        calculate_priority(find_common_item(team_sacks))
        for team_sacks in rucksack_teams
    ])


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
