# 1. Define the Data
# Format: [Source, Destination, Weight]
edges = [
    [0, 1, 10],
    [0, 2, 6],
    [0, 3, 5],
    [1, 3, 15],
    [2, 3, 4]
]
num_vertices = 4

# 2. Sort edges based on weight (The Greedy Choice)
edges.sort(key=lambda x: x[2])

# 3. Union-Find Setup
# Each node starts as its own parent (its own set)
parent = list(range(num_vertices))

def find(i):
    """Finds the root of the set node i belongs to (with Path Compression)."""
    if parent[i] == i:
        return i
    # Path Compression: updates parent to the root for next time
    parent[i] = find(parent[i])
    return parent[i]

def union(i, j):
    """Connects the sets containing i and j."""
    root_i = find(i)
    root_j = find(j)
    if root_i != root_j:
        parent[root_i] = root_j
        return True
    return False

# 4. Execute Kruskal's Algorithm
mst = []
total_weight = 0

for u, v, w in edges:
    # If find(u) != find(v), they are in different components (no cycle)
    if union(u, v):
        mst.append([u, v, w])
        total_weight += w

# 5. Output the Results
print("--- Minimum Spanning Tree ---")
print("Edge \tWeight")
for u, v, w in mst:
    print(f"{u} - {v} \t{w}")
print(f"Total MST Weight: {total_weight}")