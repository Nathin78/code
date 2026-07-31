from collections import defaultdict, deque

def topological_sort(v, edges):
    adj = defaultdict(list)
    in_degree = [0] * v
    for u, w in edges:
        adj[u].append(w)
        in_degree[w] += 1
    q = deque([i for i in range(v) if in_degree[i] == 0])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nxt in adj[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0: q.append(nxt)
    return order if len(order) == v else []

if __name__ == "__main__":
    print(topological_sort(4, [[0,1], [0,2], [1,3], [2,3]]))
