class Kruskal:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [] # Stores [u, v, w]

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Find the 'Set' of an element (with Path Compression)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        # Path Compression: Connects node directly to the root
        parent[i] = self.find(parent, parent[i])
        return parent[i]

    # Union of two sets
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        # Union by Rank: Keep the tree flat
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def run_kruskal(self):
        result = [] # Stores the MST
        i, e = 0, 0 # Index for sorted edges and MST edges

        # 1. GREEDY STEP: Sort all edges by weight
        self.graph.sort(key=lambda item: item[2])

        parent = []
        rank = []

        # Create V single-element sets
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # 2. Process edges until MST has V-1 edges
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge doesn't cause a cycle
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        # Print Result
        print("Edge \tWeight")
        for u, v, weight in result:
            print(f"{u} - {v} \t{weight}")

# --- Execution ---
g = Kruskal(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.run_kruskal()