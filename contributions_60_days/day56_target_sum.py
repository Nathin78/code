def find_target_sum_ways(nums, target):
    dp = {0: 1}
    for num in nums:
        next_dp = {}
        for s in dp:
            next_dp[s + num] = next_dp.get(s + num, 0) + dp[s]
            next_dp[s - num] = next_dp.get(s - num, 0) + dp[s]
        dp = next_dp
    return dp.get(target, 0)

if __name__ == "__main__":
    print(find_target_sum_ways([1, 1, 1, 1, 1], 3))
