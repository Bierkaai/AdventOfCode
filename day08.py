


class NumberDisplayDeducer(object):

    def __init__(self, digitstr):
        self.inputstr, self.outputstr = (x.strip() for x in digitstr.split("|"))
        self.inputlist = self.inputstr.split()
        self.outputlist = self.outputstr.split()

