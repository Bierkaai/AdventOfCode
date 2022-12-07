from abc import abstractmethod, ABC

from aocd.models import Puzzle

ROOT_NAME = "/"

DAY = 7
YEAR = 2022


class FileSystemNode(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def total_size(self):
        return 0

class Directory(FileSystemNode):

    def total_size(self):
        return 0

class File(FileSystemNode):

    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    def total_size(self):
        return self.size


class FileSystemNav:

    def __init__(self, root: str = ROOT_NAME):
        self.root = Directory(root)
        self.pwd = self.root

    def cd(self, dir: str):
        pass

    def add_file(self, name, size):
        pass

    def add_dir(self, name):
        pass

    def lsal(self):
        return pwd.total_size()


def solve_a(data):
    pass


def solve_b(data):
    pass


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
