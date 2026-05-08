class Graph:

    def __init__(self):

        self.graph = []

    # Add Edge
    def addEdge(self, u, v, w):

        self.graph.append([u, v, w])

    # Find Parent
    def find(self, parent, node):

        if parent[node] == node:
            return node

        return self.find(parent, parent[node])

    # Union
    def union(self, parent, x, y):

        parent[x] = y

    # Kruskal Algorithm
    def kruskal(self):

        result = []

        # Sort edges according to weight
        self.graph.sort(key=lambda edge: edge[2])

        # Create parent dictionary
        parent = {}

        # Get all unique vertices
        vertices = set()

        for u, v, w in self.graph:

            vertices.add(u)
            vertices.add(v)

        # Initially every node is parent of itself
        for vertex in vertices:
            parent[vertex] = vertex

        edgeCount = 0
        index = 0

        # MST contains V-1 edges
        while edgeCount < len(vertices) - 1:

            u, v, w = self.graph[index]

            index += 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            # Avoid cycle
            if x != y:

                result.append([u, v, w])

                self.union(parent, x, y)

                edgeCount += 1

        # Print MST
        print("Edges in Minimum Spanning Tree:\n")

        totalCost = 0

        for u, v, w in result:

            print(u, "--", v, "=", w)

            totalCost += w

        print("\nMinimum Cost =", totalCost)


# ------------------------------------------------
# Graph Visualization
#
#         10
#     A -------- B
#     | \        |
#   6 |  \5      | 15
#     |   \      |
#     C -------- D
#           4
#
# ------------------------------------------------


g = Graph()

g.addEdge('A', 'B', 10)
g.addEdge('A', 'C', 6)
g.addEdge('A', 'D', 5)
g.addEdge('B', 'D', 15)
g.addEdge('C', 'D', 4)

g.kruskal()