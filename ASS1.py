class Graph:

    def __init__(self):

        self.graph = {}

    # Add Edge
    def addEdge(self, u, v):

        # Create node if not present
        if u not in self.graph:
            self.graph[u] = []

        # Create destination node also
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)

    # Display Graph
    def display(self):

        print("Adjacency List Representation:\n")

        for node in self.graph:
            print(node, "->", self.graph[node])

    # BFS Traversal
    def BFS(self, start):

        visited = []
        queue = []

        visited.append(start)
        queue.append(start)

        print("\nBFS Traversal:")

        while queue:

            node = queue.pop(0)

            print(node, end=" ")

            for neighbour in self.graph[node]:

                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

    # DFS Traversal
    def DFS(self, start):

        visited = []

        print("\n\nDFS Traversal:")

        self.DFS_Helper(start, visited)

    # DFS Helper Function
    def DFS_Helper(self, node, visited):

        visited.append(node)

        print(node, end=" ")

        for neighbour in self.graph[node]:

            if neighbour not in visited:
                self.DFS_Helper(neighbour, visited)


# ---------------------------------------------------
# Graph Visualization
#
#         A
#       /   \
#      B     C
#     / \     \
#    D   E ---- F
#
# Edges:
# A -> B
# A -> C
# B -> D
# B -> E
# C -> F
# E -> F
# ---------------------------------------------------


# Create Graph
g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'D')
g.addEdge('B', 'E')
g.addEdge('C', 'F')
g.addEdge('E', 'F')

# Display Graph
g.display()

# BFS Traversal
g.BFS('A')

# DFS Traversal
g.DFS('A')