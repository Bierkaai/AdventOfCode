
from models.binary import Bits

from aocd.models import Puzzle

DAY = 3
YEAR = 2021


def tokenize_to_str_list(long_str: str):
    return [x for x in long_str.splitlines(keepends=False)]

def transpose_str_list(str_list: list):
    return ["".join(x) for x in zip(*str_list)]

def get_most_common_bit(bitstr: str):
    if bitstr.count("1") > (len(bitstr) / 2):
        return "1"
    return "0"


def solve_a(data):
    # transpose the input (rows become columns)
    transposed_str_list = transpose_str_list(
        tokenize_to_str_list(data)
    )
    # find the most common bit in each column
    gamma_b = Bits(bit_str="".join([get_most_common_bit(x) for x in transposed_str_list]))
    epsilon_b = ~gamma_b
    return int(gamma_b) * int(epsilon_b)



def solve_b(data):
    return None


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
