from abc import ABC, abstractmethod
from dataclasses import dataclass

from aocd.models import Puzzle

DAY = 2
YEAR = 2021


@dataclass
class BaseSubmarine(ABC):
    depth: int = 0
    position: int = 0

    @abstractmethod
    def parse_command(self, command: str):
        pass

    @property
    def multiplied_pos_indicator(self):
        return self.depth * self.position

    def extract_command_parameters(self, command):
        direction, amount_str = command.split()
        amount = int(amount_str)
        return amount, direction


class Submarine(BaseSubmarine):
    def parse_command(self, command: str):
        amount, direction = self.extract_command_parameters(command)
        if direction == "forward":
            self.position += amount
        if direction == "down":
            self.depth += amount
        if direction == "up":
            self.depth -= amount


class SubmarineB(BaseSubmarine):
    aim: int = 0


def solve_a(data):
    s = Submarine()
    for line in data.splitlines(keepends=False):
        s.parse_command(line)
    return s.multiplied_pos_indicator


def solve_b(data):
    return None


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
