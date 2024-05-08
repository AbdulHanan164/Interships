class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
    def find(self, element):
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
def find_connected_components(graph):
    num_vertices = len(graph)
    disjoint_set = DisjointSet(num_vertices)
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] == 1:
                disjoint_set.union(i, j)
    components = {}
    for i in range(num_vertices):
        root = disjoint_set.find(i)
        if root in components:
            components[root].append(i)
        else:
            components[root] = [i]
    return list(components.values())
graph = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]
print(find_connected_components(graph))
