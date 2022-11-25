from collections import deque


class Parser(object):

    VALID_PAIRS = (
        ("(", ")"),
        ("[", "]"),
        ("{", "}"),
        ("<", ">")
    )

    SYNTAX_ERROR_SCORES = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    def __init__(self):
        self.closing_dict = dict(self.VALID_PAIRS)
        # This is the weirdest tuple comprehension ever... but it works
        self.valid_chars = tuple((p for pair in self.VALID_PAIRS for p in pair))
        self.open_stack = deque()

    def read_char(self, c):
        if c not in self.valid_chars:
            raise SyntaxError()
        if c in self.closing_dict:
            self.open_stack.append(self.closing_dict[c])
            return
        expected_char = self.open_stack.pop()
        if c != expected_char:
            raise SyntaxError(f"Expected '{expected_char}', but found '{c}'")




