from collections import defaultdict
from pathlib import Path


def read_data():
    input_file = Path("input.txt")
    text = input_file.read_text()
    lines = text.split("\n")
    lines = list(map(lambda x: x.split(" "), lines))
    nb_ver, nb_edge = list(map(int, lines[0]))
    edges = []
    for i in range(nb_edge):
        edges.append(list(map(int, lines[i + 1])))
    return nb_ver, edges

class Graph:
    def __init__(self, nb_vertical):
        self.graph = defaultdict(list)
        self.nb_vertical = nb_vertical

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, trace):
        print("visit v=", v)
        for i in range(self.nb_vertical):
            if (trace[i] == -1) and (i in self.graph[v]):
                trace[i] = v
                trace = self.dfs_util(i, trace)
        return trace

    def dfs(self, v):
        trace = defaultdict(lambda: -1)
        trace = self.dfs_util(v, trace)
        return trace

    def get_result_dfs(self, node_from, node_to, trace):
        if trace[node_to] == -1:
            return []
        travel = []
        while True:
            travel.append(node_to)
            if node_from == node_to:
                break
            node_to = trace[node_to]
        return travel[::-1]


nb_ver, edges = read_data()
g = Graph(nb_ver)
for edge in edges:
    print(edge)
    g.add_edge(edge[0], edge[1])

print("Following is DFS from (starting from vertex 2)")
trace = g.dfs(0)
print(trace)
print(g.get_result_dfs(0, 3, trace))