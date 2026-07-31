# Climbing Stairs - DP (count ways to reach nth step)
def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b

for i in range(1, 8):
    print(f"climb_stairs({i}) = {climb_stairs(i)}")
# 1,2,3,5,8,13,21
