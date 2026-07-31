# Dijkstra Shortest Path Algorithm
import heapq

def dijkstra(graph, start):
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist

graph = {
    "A": [("B",1),("C",4)],
    "B": [("C",2),("D",5)],
    "C": [("D",1)],
    "D": []
}
print(dijkstra(graph, "A"))  # A:0, B:1, C:3, D:4
