from aocd.models import Puzzle

ROOT_NAME = "/"

DAY = 7
YEAR = 2022


class FileSystemNode:

    def __init__(self, name: str):
        self.name = name


class FileSystemNav:

    def __init__(self, root: str = ROOT_NAME):
        self.root = FileSystemNode(root)
        self.pwd = self.root


def solve_a(data):
    pass


def solve_b(data):
    pass


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
