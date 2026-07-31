# Topological Sort using DFS (Kahns algorithm)
from collections import deque

def topological_sort(vertices, edges):
    in_degree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    queue = deque([v for v in in_degree if in_degree[v] == 0])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return result if len(result) == vertices else []

print(topological_sort(6, [(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)]))
