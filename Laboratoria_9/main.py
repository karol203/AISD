from typing import Any


class Vertex:
    data: Any

    def __init__(self, data=None):
        self.data = data

    def __str__(self):
        return self.data


class Edge:
    vertices: set[Vertex]
    weight: float

    def __init__(self, vertex1=None, vertex2=None, weight=1.0):
        if (vertex1 and vertex2) is not None:
            self.vertices = {vertex1, vertex2}
        else:
            self.vertices = set()

    def __str__(self):
        if self.vertices is not None:
            return ' - '.join(str(self.vertices))


class Graph:
    vertices: list[Vertex]
    edges: set[Edge]

    def __init__(self):
        self.vertices = []
        self.edges = set()

    def __str__(self):
        return str(self.edges) + ' ' + str(self.vertices)

    def add_vertex(self, value):
        V = Vertex(value)
        self.vertices.append(V)

    def size(self):
        return len(self.vertices)

    def edge_size(self):
        return len(self.edges)

    def add_edge(self, vertex1, vertex2, weight=1.0):
        self.edges.add(Edge(vertex1, vertex2, weight))

    def is_edge(self, vertex1, vertex2):
        for x in self.edges:
            if {vertex1, vertex2} == x.vertices:
                return True
        return False

    def cone(self, value):
        self.add_vertex(value)
        for x in self.vertices[:-1]:
            self.add_edge(x, self.vertices[-1])

    def complete_graph(self, *values):
        self.add_vertex(values[0])
        for x in range(1, len(values)):
            self.cone(values[x])

    def adjacency_matrix(self):
        size = self.size()
        matrix = []
        for x in range(size):
            row = []
            for y in range(size):
                if self.is_edge(self.vertices[x], self.vertices[y]):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix

    def neighbours_dict(self):
        slownik = {}
        for v in self.vertices:
            neigh = []
            for e in self.edges:
                if v in e.vertices:
                    u = list(e.vertices - {v})[0]
                    neigh.append(u)
            neigh.sort(key=lambda x: self.vertices.index(x))
            slownik[v] = neigh
        return slownik

    def neighbours_dict_data(self):
        d = self.neighbours_dict()
        return {v.data: [u.data for u in lst] for v, lst in d.items()}

    def breadth_first_traversal(self, visit_func):
        if not self.vertices:
            return
        visited = set()
        queue = []
        start_v = self.vertices[0]
        visit_func(start_v)
        visited.add(start_v)
        queue.append(start_v)
        while queue:
            v = queue.pop(0)
            neighbors = []
            for candidate in self.vertices:
                if candidate != v and self.is_edge(v, candidate):
                    neighbors.append(candidate)
            for neighbour in neighbors:
                if neighbour not in visited and neighbour not in queue:
                    visit_func(neighbour)
                    visited.add(neighbour)
                    queue.append(neighbour)

    def deep_first_traversal(self, visit_func):
        if not self.vertices:
            return
        visited = set()

        def dfs_recursive(current_v):
            visit_func(current_v)
            visited.add(current_v)
            for candidate in self.vertices:
                if candidate != current_v and self.is_edge(current_v, candidate):
                    if candidate not in visited:
                        dfs_recursive(candidate)

        if len(self.vertices) > 0:
            dfs_recursive(self.vertices[0])

    def from_adjacency_matrix(self, matrix: list[list[int]]):
        self.vertices.clear()
        self.edges.clear()
        rows = len(matrix)
        for i in range(rows):
            self.add_vertex(f"v{i}")
        for i in range(rows):
            for j in range(i + 1, rows):
                if matrix[i][j] != 0:
                    self.add_edge(self.vertices[i], self.vertices[j])


G = Graph()
assert G.size() == 0
assert G.edge_size() == 0
G.add_vertex('v0')
assert G.size() == 1
assert G.edge_size() == 0
G.add_vertex('v1')
G.cone('v2')
assert G.edge_size() == 2
assert G.is_edge(G.vertices[0], G.vertices[1]) == False
G.add_vertex('v3')
G.add_edge(G.vertices[0], G.vertices[3])
G_complete = Graph()
G_complete.complete_graph('x0', 'x1', 'x2', 'x3')
assert G_complete.size() == 4
assert G_complete.edge_size() == 6
assert G.adjacency_matrix() == [[0, 0, 1, 1], [0, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
assert G_complete.adjacency_matrix() == [[0, 1, 1, 1, ], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
assert G.neighbours_dict_data() == {'v0': ['v2', 'v3'], 'v1': ['v2'], 'v2': ['v0', 'v1'], 'v3': ['v0']}
assert G_complete.neighbours_dict_data() == {'x0': ['x1', 'x2', 'x3'], 'x1': ['x0', 'x2', 'x3'],
                                             'x2': ['x0', 'x1', 'x3'], 'x3': ['x0', 'x1', 'x2']}
G_breadth = []
G.breadth_first_traversal(G_breadth.append)
assert [x.data for x in G_breadth] == ['v0', 'v2', 'v3', 'v1']
G_deep = []
G.deep_first_traversal(G_deep.append)
assert [x.data for x in G_deep] == ['v0', 'v2', 'v1', 'v3']
G = Graph()
G.from_adjacency_matrix([[0, 1, 1, 0, 0], [1, 0, 1, 0, 0], [1, 1, 0, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]])
assert G.size() == 5
G_breadth = []
G.breadth_first_traversal(G_breadth.append)
assert [x.data for x in G_breadth] == ['v0', 'v1', 'v2', 'v3', 'v4']
G_deep = []
G.deep_first_traversal(G_deep.append)
assert [x.data for x in G_deep] == ['v0', 'v1', 'v2', 'v3', 'v4']