from collections import defaultdict, deque

def can_finish(numCourses, prerequisites):
    adj = defaultdict(list)
    in_degree = [0] * numCourses
    for dest, src in prerequisites:
        adj[src].append(dest)
        in_degree[dest] += 1
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    visited = 0
    while queue:
        node = queue.popleft()
        visited += 1
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0: queue.append(neighbor)
    return visited == numCourses

if __name__ == "__main__":
    print(can_finish(2, [[1, 0]]))
