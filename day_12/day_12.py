import networkx

from collections import Counter

START_CAVE_NAME = 'start'
END_CAVE_NAME = 'end'

INPUT_FILE = "../input/12.txt"


class CaveNetwork(object):

    def __init__(self, in_rep):
        if isinstance(in_rep, str):
            self.strrep = in_rep
            # make an ebunch from the edges string representation
            self.edge_list = [tuple(s.split("-")) for s in in_rep.split("\n")]
        elif isinstance(in_rep, list):
            self.strrep = "\n".join(in_rep)
            self.edge_list = [tuple(s.split("-")) for s in in_rep]
        else:
            raise TypeError(f"unsupported input type {type(in_rep)}")

        self.graph = networkx.Graph()

        # add edges to internal graph representation
        self.graph.add_edges_from(self.edge_list)

        self.small_caves = {n for n in self.graph.nodes if str(n).islower()}

    @property
    def n_caves(self):
        return self.graph.number_of_nodes()

    def find_paths(self, start_cave=START_CAVE_NAME, end_cave=END_CAVE_NAME, path=tuple()):

        def is_explorable(cave):
            if cave not in path:
                return True
            if cave not in self.small_caves:
                return True
            return False
        # append this node to the path
        path_to_here = path + (start_cave,)

        # if this cave is the end, return the path
        if start_cave == end_cave:
            return {path_to_here}

        # find all explorable caves, based on is_explorable function
        explorable_caves = [
            n for n in self.graph.neighbors(start_cave) if is_explorable(n)
        ]

        # nothing left to explore? We are on a dead end
        if len(explorable_caves) < 1:
            return set()

        # for each node, return all paths that lead to the end
        return set.union(*[
            self.find_paths(
                start_cave=neighbor,
                end_cave=end_cave,
                path=path_to_here
            )
            for neighbor in explorable_caves
        ])

    def count_paths(self, start_cave=START_CAVE_NAME, end_cave=END_CAVE_NAME):
        return len(self.find_paths(start_cave=start_cave, end_cave=end_cave))


if __name__ == "__main__":
    with open(INPUT_FILE, 'r') as f_obj:
        in_str = "".join(f_obj)
    cn = CaveNetwork(in_str)

    print(f"Input cave network has {cn.count_paths()} paths")
