
SIMPLE_DIGITS = (1,4,7,8)

class NumberDisplay(object):

    def __init__(self, strrep):
        self.strrep = strrep

    @property
    def bitstring(self) -> str:
        pass

    def __len__(self):
        return len(self.strrep)


class NumberDisplayDeducer(object):

    def __init__(self, digitstr):
        self.inputstr, self.outputstr = (x.strip() for x in digitstr.split("|"))
        self.inputlist = self.inputstr.split()
        self.outputlist = self.outputstr.split()

    def count_in_output(self, n):
        if n == 1:
            return sum(len(x) == 2 for x in self.outputlist)
        if n == 4:
            return sum(len(x) == 4 for x in self.outputlist)
        if n == 7:
            return sum(len(x) == 3 for x in self.outputlist)
        if n == 8:
            return sum(len(x) == 7 for x in self.outputlist)


def count_numbers_in_outputs(lines):
    summed = 0

    for line in lines:
        if len(line) > 1:
            print(f"LINE: '{line}'")
            ndd = NumberDisplayDeducer(line)
            summed += sum([ndd.count_in_output(d) for d in SIMPLE_DIGITS])

    return summed

if __name__ == "__main__":
    lines = open("./input/08.txt", 'r')
    print(count_numbers_in_outputs(lines))

