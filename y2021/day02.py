from abc import ABC, abstractmethod
from dataclasses import dataclass

from aocd.models import Puzzle

DAY = 2
YEAR = 2021


def extract_command_parameters(command):
    direction, amount_str = command.split()
    amount = int(amount_str)
    return amount, direction


@dataclass
class BaseSubmarine(ABC):
    depth: int = 0
    position: int = 0

    @property
    def multiplied_pos_indicator(self):
        return self.depth * self.position

    def parse_command(self, command: str):
        amount, direction = extract_command_parameters(command)
        if direction == "forward":
            self.forward(amount)
        if direction == "down":
            self.down(amount)
        if direction == "up":
            self.up(amount)

    @abstractmethod
    def forward(self, amount):
        pass

    @abstractmethod
    def down(self, amount):
        pass

    @abstractmethod
    def up(self, amount):
        pass


class Submarine(BaseSubmarine):

    def down(self, amount):
        self.depth += amount

    def up(self, amount):
        self.depth -= amount

    def forward(self, amount):
        self.position += amount


class SubmarineB(BaseSubmarine):
    aim: int = 0

    def forward(self, amount):
        self.depth += self.aim * amount
        self.position += amount

    def down(self, amount):
        self.aim += amount

    def up(self, amount):
        self.aim -= amount


def solve_a(data):
    s = Submarine()
    for line in data.splitlines(keepends=False):
        s.parse_command(line)
    return s.multiplied_pos_indicator


def solve_b(data):
    s = SubmarineB()
    for line in data.splitlines(keepends=False):
        s.parse_command(line)
    return s.multiplied_pos_indicator


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
