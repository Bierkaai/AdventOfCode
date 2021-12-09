from collections import deque

INPUT_FILE = "./input/09.txt"
BUFFER_LENGTH = 3

class GridBuilder(object):

    def __init__(self):
        self.linebuffer = deque(maxlen=BUFFER_LENGTH)
        for i in range(BUFFER_LENGTH):
            self.linebuffer.append("")

    def get_linebuffer_slice(self, buffer_id, start, end):
        try:
            line = self.linebuffer[buffer_id]
        except IndexError:
            # if this index is not in the line buffer, return empty
            return []
        if start < 0:
            start = 0
        if end > len(line):
            end = len(line)
        return [int(x) for x in line[start:end]]

    def get_neighborhood(self, pos):
        # Returns the immediate neighborhood for the given pos on the middle line in the buffer
        return set(
            self.get_linebuffer_slice(0, pos-1, pos+2) +
            self.get_linebuffer_slice(1, pos-1, pos) +
            self.get_linebuffer_slice(1, pos+1, pos+2) +
            self.get_linebuffer_slice(2, pos-1, pos+2)
        )

    def get_neighborhood_min(self, pos):
        return min(self.get_neighborhood(pos))

    def report_lows(self):
        # reporting the lowest points in current line
        line_in_scope = self.linebuffer[1]
        print(f"Reporting lows from line: {line_in_scope}")
        for i, n in enumerate(line_in_scope):
            print(f"i = {i}, number = {n}")
            num = int(n)
            neighborhood = self.get_neighborhood(i)
            neighborhood_min = self.get_neighborhood_min(i)
            print(f"Neighborhood = {neighborhood} | minimum = {neighborhood_min}")
            if num < neighborhood_min:
                print(f"{num} is a minimum in its neighborhood")
                yield num


    def add_line(self, l):
        # add line to linebuffer
        self.linebuffer.append(l)

        # check if we already have a previous line
        if len(self.linebuffer) > 1:
            return list(self.report_lows())
        return []


if __name__ == "__main__":

    with open(INPUT_FILE, 'r') as f_obj:
        for line in f_obj:
            gb.add_line(line)

