# Coin Change - minimum coins to make amount
def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1

print(coin_change([1, 5, 6, 9], 11))  # 2
print(coin_change([2], 3))            # -1
