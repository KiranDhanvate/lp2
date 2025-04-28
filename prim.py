class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in vertices}

    def add_edge(self, u, v, weight):
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))

    def prim(self):
        start_vertex = self.vertices[0]
        visited = set()
        edges = []
        mst = []

        visited.add(start_vertex)
        for neighbor, weight in self.adjacency_list[start_vertex]:
            edges.append((weight, start_vertex, neighbor))

        while edges and len(visited) < len(self.vertices):
            edges.sort()
            weight, u, v = edges.pop(0)

            if v not in visited:
                visited.add(v)
                mst.append((u, v, weight))
                for neighbor, w in self.adjacency_list[v]:
                    if neighbor not in visited:
                        edges.append((w, v, neighbor))

        return mst

# -------- Main Program --------

# Take input
# Example usage
vertices = [0, 1, 2, 3]
g = Graph(vertices)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 10)
g.add_edge(0, 3, 3)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 4)

minimum_spanning_tree = g.prim()
print("Minimum Spanning Tree (Prim's):")
for edge in minimum_spanning_tree:
    print(edge)
