from collections import deque

# 1. The Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 2. Recursive DFS
def dfs(graph, node, visited=None):
    if visited is None:
        visited = []

    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph.get(node, []):
            dfs(graph, neighbour, visited)
    return visited

# 3. Recursive BFS 
def bfs(graph, queue, visited):
    if not queue:
        return visited

    node = queue.popleft()
    print(node, end=" ")

    for neighbour in graph.get(node, []):
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)

    return bfs(graph, queue, visited)

# --- Execution ---
print("DFS Traversal:")
dfs(graph, 'A')

print("\n\nBFS Traversal:")
# BFS needs a starting setup: visited list and a deque queue
start_node = 'A'
bfs(graph, deque([start_node]), [start_node])