import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_d, curr_node = heapq.heappop(pq)
        if curr_d > distances[curr_node]: continue
        for neighbor, weight in graph[curr_node].items():
            d = curr_d + weight
            if d < distances[neighbor]:
                distances[neighbor] = d
                heapq.heappush(pq, (d, neighbor))
    return distances

if __name__ == "__main__":
    g = {'A': {'B': 1, 'C': 4}, 'B': {'C': 2}, 'C': {}}
    print(dijkstra(g, 'A'))
