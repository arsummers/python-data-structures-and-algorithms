class Graph:
    def __init__(self):
        self._vertices = []

    def add_vertex(self, value):
        vert = Vertex(value)
        self._vertices.append(vert)
        return vert

    def get_vertices(self):
        return self._vertices or None

    def add_edge(self, vert1, vert2, weight=0):
        if vert1 in self._vertices and vert2 in self._vertices:
            vert1.neighbors.append(Edge(vert2, weight))

    def get_neighbors(self, vertex):
        return vertex.neighbors

    def __len__(self):
        return len(self._vertices)

class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False