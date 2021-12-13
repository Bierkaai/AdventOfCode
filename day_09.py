from collections import deque

INPUT_FILE = "./input/09.txt"
# TODO: this falsely suggests you can change the neighborhood size. This is not the case yet
NEIGHBORHOOD_SIZE = 3

class GridBuilder(object):

    def __init__(self):
        self.linebuffer = deque(maxlen=NEIGHBORHOOD_SIZE)
        for i in range(NEIGHBORHOOD_SIZE):
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
        # TODO: implement variable neighborhood if needed
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

        for i, n in enumerate(line_in_scope):
            num = int(n)
            neighborhood = self.get_neighborhood(i)
            neighborhood_min = self.get_neighborhood_min(i)
            if num < neighborhood_min:
                yield num

    def add_line(self, l):
        # add line to linebuffer
        self.linebuffer.append(l)

        # check if we already have a previous line
        if len(self.linebuffer) > 1:
            return list(self.report_lows())
        return []

def get_risk_level(lines):
    risk_level = 0
    gb = GridBuilder()
    for line in lines:
        new_risks = gb.add_line(line.strip())
        risk_level += sum(new_risks) + len(new_risks)
    # This sucks, need to add an empty line at the end to trigger calculation of bottom line
    new_risks = gb.add_line("")
    risk_level += sum(new_risks) + len(new_risks)
    return risk_level

if __name__ == "__main__":
    risk_level = 0
    gb = GridBuilder()
    with open(INPUT_FILE, 'r') as f_obj:
        print(get_risk_level(f_obj))


