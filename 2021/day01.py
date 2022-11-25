from aocd.models import Puzzle

if __name__ == "__main__":
    p = Puzzle(year=2021, day=1)
    print(p.example_data)
    print(p.easter_eggs)