def print_array(a):
    for i in a:
        print(i)

class Graph:

    def __init__(self, number_vertical):
        self.number_vertical = number_vertical
        # self.adjacency_matrix = np.full((number_vertical, number_vertical), False)
        self.adjacency_matrix = [[False for i in range(number_vertical)] for j in range(number_vertical)]

    def add_edge(self, u, v):
        self.adjacency_matrix[u][v] = True
        self.adjacency_matrix[v][u] = True

    def find_connected_component(self):
        print_array(self.adjacency_matrix)
        for k in range(self.number_vertical):
            for u in range(self.number_vertical):
                for v in range(self.number_vertical):
                    self.adjacency_matrix[u][v] = self.adjacency_matrix[u][v] or (self.adjacency_matrix[u][k] \
                                                                              and self.adjacency_matrix[k][v])
        # free = np.full((self.number_vertical, ), True)
        free = [True for i  in range(self.number_vertical)]
        connected_components = []
        for i in range(self.number_vertical):
            components = set()
            if free[i]:
                for j in range(self.number_vertical):
                    if self.adjacency_matrix[i][j]:
                        components.add(j)
                        free[j] = False
            if len(components) != 0:
                connected_components.append((list(components)))
        return connected_components

g = Graph(8)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(7, 7)
print(g.find_connected_component())


