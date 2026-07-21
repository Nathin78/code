from collections import deque

def max_sliding_window(nums, k):
    q = deque()
    res = []
    for i, cur in enumerate(nums):
        while q and nums[q[-1]] <= cur: q.pop()
        q.append(i)
        if q[0] == i - k: q.popleft()
        if i >= k - 1: res.append(nums[q[0]])
    return res

if __name__ == "__main__":
    print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
