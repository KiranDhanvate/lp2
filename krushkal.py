class Graph:  
    def __init__(self, vertices):  
        self.vertices = vertices  
        self.edges = []  
        self.adjacency_list = {v: [] for v in vertices}  
  
    def add_edge(self, u, v, weight):  
        self.edges.append((u, v, weight))  
        self.adjacency_list[u].append((v, weight))  
        self.adjacency_list[v].append((u, weight))  
  
    def find_parent(self, parent, i):  
        if parent[i] == i:  
            return i  
        return self.find_parent(parent, parent[i])  
  
    def union(self, parent, rank, x, y):  
        root_x = self.find_parent(parent, x)  
        root_y = self.find_parent(parent, y)  
        if rank[root_x] < rank[root_y]:  
            parent[root_x] = root_y  
        elif rank[root_x] > rank[root_y]:  
            parent[root_y] = root_x  
        else:  
            parent[root_y] = root_x  
            rank[root_x] += 1  
  
    def kruskal(self):  
        minimum_spanning_tree = set()  
        parent = {}  
        rank = {}  
        for v in self.vertices:  
            parent[v] = v  
            rank[v] = 0  
        sorted_edges = sorted(self.edges, key=lambda x: x[2])  
        for edge in sorted_edges:  
            u, v, weight = edge  
            root_u = self.find_parent(parent, u)  
            root_v = self.find_parent(parent, v)  
            if root_u != root_v:  
                minimum_spanning_tree.add(edge)  
                self.union(parent, rank, root_u, root_v)  
        return minimum_spanning_tree  
vertices = [0, 1, 2, 3]  
g = Graph(vertices)  
g.add_edge(0, 1, 5)  
g.add_edge(0, 2, 10)  
g.add_edge(0, 3, 3)  
g.add_edge(1, 3, 1)  
g.add_edge(2, 3, 4)  
minimum_spanning_tree = g.kruskal()  
print(minimum_spanning_tree)