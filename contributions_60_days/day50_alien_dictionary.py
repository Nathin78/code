from collections import defaultdict, deque

def alien_order(words):
    adj = {c: set() for w in words for c in w}
    in_degree = {c: 0 for c in adj}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]: return ""
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break

    queue = deque([c for c in in_degree if in_degree[c] == 0])
    res = []
    while queue:
        c = queue.popleft()
        res.append(c)
        for neighbor in adj[c]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0: queue.append(neighbor)
    return "".join(res) if len(res) == len(in_degree) else ""

if __name__ == "__main__":
    print(alien_order(["wrt", "wrf", "er", "ett", "rftt"]))
