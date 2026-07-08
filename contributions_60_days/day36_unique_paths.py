def unique_paths(m, n):
    dp = [1] * n
    for _ in range(m - 1):
        for j in range(1, n): dp[j] += dp[j - 1]
    return dp[-1]

if __name__ == "__main__":
    print(unique_paths(3, 7))
