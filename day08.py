import string

INPUT_FILE = "./input/08.txt"

BITLENGTH = 7

SIMPLE_DIGITS = (1, 4, 7, 8)
SIX_SEGMENT_DIGITS = (0, 9, 6)
FIVE_SEGMENT_DIGITS = (2, 3, 5)
DIGIT_LENGTH_REPRESENTATION = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

reverse_map = {v: k for k, v in DIGIT_LENGTH_REPRESENTATION.items()}


class NumberDisplayDeducer(object):

    def __init__(self, digitstr):
        self.inputstr, self.outputstr = (x.strip() for x in digitstr.split("|"))
        self.inputlist = self.inputstr.split()
        self.outputlist = self.outputstr.split()

        self.inputsets = [set([char for char in num]) for num in self.inputlist]

        self.deduce_numbers()
        self.inverted_number_map = {"".join(sorted(list(v))): k for k, v in self.nmap.items()}

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
        self.nmap = self.get_simple_number_map()
        self.find_other_numbers()

    def find_other_numbers(self):
        for n in self.inputsets:
            if len(n) == 6:
                # if 6 segments, and union with 1 yields 8, it is a 6
                if n.union(self.nmap[1]) == self.nmap[8]:
                    self.nmap[6] = n
                # if it is not a 6, and union with 4 yields 8, it is a 0
                elif n.union(self.nmap[4]) == self.nmap[8]:
                    self.nmap[0] = n
                # otherwise, it is a 9
                else:
                    self.nmap[9] = n
            elif len(n) == 5:
                # lenght = 5 and this is a superset of 1, it is a 3
                if n.issuperset(self.nmap[1]):
                    self.nmap[3] = n
                # if it is not 3 and the union with 4 yields 8, it is a 2
                elif n.union(self.nmap[4]) == self.nmap[8]:
                    self.nmap[2] = n
                # otherwise, it is a 5
                else:
                    self.nmap[5] = n

    def get_output_number(self):
        # Look up each string (sorted) in the output in the inverted number map
        # paste the resulting numbers together using join
        # interpret resulting string as int
        return int(
            "".join([str(self.inverted_number_map[strrep]) for strrep in
                     ["".join(sorted(n)) for n in self.outputlist]
                     ])
        )


def count_numbers_in_outputs(lines):
    summed = 0

    for line in lines:
        if len(line) > 1:
            ndd = NumberDisplayDeducer(line)
            summed += sum([ndd.count_in_output(d) for d in SIMPLE_DIGITS])

    return summed

def sum_translated_numbers(lines):
    summed = 0

    for line in lines:
        if len(line) > 1:
            ndd = NumberDisplayDeducer(line)
            summed += ndd.get_output_number()
    return summed


if __name__ == "__main__":
    with open(INPUT_FILE, 'r') as f_obj:
        lines = f_obj.readlines()
    #lines = open(INPUT_FILE, 'r')
    print("Answer 1: ", count_numbers_in_outputs(lines))
    #lines.close()

    #lines = open(INPUT_FILE, 'r')
    print("Answer 2: ", sum_translated_numbers(lines))
    #lines.close()


