import string

BITLENGTH = 7

SIMPLE_DIGITS = (1, 4, 7, 8)
DIGIT_LENGTH_REPRESENTATION = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

reverse_map = {v: k for k, v in DIGIT_LENGTH_REPRESENTATION.items()}

class NumberDisplay(object):

    def __init__(self, strrep):
        self.strrep = strrep
        self.bitstring = self.calc_bitstring()
        self.intrep = int(self.bitstring, 2)

    def calc_bitstring(self) -> str:
        result = ""
        for letter in string.ascii_lowercase[:7]:
            if letter in self.strrep:
                result = "1" + result
            else:
                result = "0" + result
        return result

    @property
    def is_simple_digit(self):
        return

    def __int__(self):
        return self.intrep

    def __xor__(self, other) -> int:
        return int(self) ^ int(other)

    def __or__(self, other) -> int:
        return int(self) | int(other)

    def __invert__(self):
        return int(self) ^ (2 ** BITLENGTH - 1)

    def __len__(self):
        return len(self.strrep)

    def __eq__(self, other):
        return int(self) == int(other)


class NumberDisplayDeducer(object):

    def __init__(self, digitstr):
        self.inputstr, self.outputstr = (x.strip() for x in digitstr.split("|"))
        self.inputlist = self.inputstr.split()
        self.outputlist = self.outputstr.split()

        self.inputsets = [set([char for char in num]) for num in self.inputlist]

    def count_in_output(self, n):
        if n not in SIMPLE_DIGITS:
            raise ValueError(f"{n} not a simply deducible number")
        else:
            return sum(len(x) == reverse_map[n] for x in self.outputlist)

    def get_simple_number_map(self):
        simple_number_map = {}
        for numset in self.inputsets:
            numset_len = len(numset)
            if numset_len in DIGIT_LENGTH_REPRESENTATION:
                simple_number_map[DIGIT_LENGTH_REPRESENTATION[numset_len]] = numset
        return simple_number_map

    def deduce_numbers(self):
        nmap = self.get_simple_number_map()
        top = self.deduce_top_segment(nmap[7], nmap[1])


    def deduce_top_segment(self, seven, one):
        print(seven)
        print(one)
        return seven.difference(one)




def count_numbers_in_outputs(lines):
    summed = 0

    for line in lines:
        if len(line) > 1:
            ndd = NumberDisplayDeducer(line)
            summed += sum([ndd.count_in_output(d) for d in SIMPLE_DIGITS])

    return summed


if __name__ == "__main__":
    lines = open("./input/08.txt", 'r')
    print(count_numbers_in_outputs(lines))
