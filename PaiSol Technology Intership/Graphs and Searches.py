#TASK 2 Design and Implement a Graph Class
class Graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    def add_edge(self, start, end):
        if start in self.graph:
            self.graph[start].append(end)
        else:
            self.graph[start] = [end]
    def depth_first_traversal(self, start):
        visited = set()
        def dfs(node):
            visited.add(node)
            print(node, end=" ")
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(start)
    def breadth_first_traversal(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                queue.extend(self.graph.get(node, []))
# Example usage:
g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
print("Depth First Traversal:")
g.depth_first_traversal(2)
print("\nBreadth First Traversal:")
g.breadth_first_traversal(2)