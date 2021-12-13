from unittest import TestCase

EXAMPLE_INPUT = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

all_paths_in_example = {
    ["start", "A", "b", "A", "c", "A", "end"],
    ["start", "A", "b", "A", "end"],
    ["start", "A", "b", "end"],
    ["start", "A", "c", "A", "b", "A", "end"],
    ["start", "A", "c", "A", "b", "end"],
    ["start", "A", "c", "A", "end"],
    ["start", "A", "end"],
    ["start", "b", "A", "c", "A", "end"],
    ["start", "b", "A", "end"],
    ["start", "b", "end"]
}

class TestCaveNetwork(TestCase):
    pass
