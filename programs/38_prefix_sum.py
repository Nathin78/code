# Prefix Sum for range sum queries
class PrefixSum:
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)
        for i, n in enumerate(nums):
            self.prefix[i+1] = self.prefix[i] + n

    def range_sum(self, left, right):
        return self.prefix[right+1] - self.prefix[left]

ps = PrefixSum([1, 2, 3, 4, 5])
print(ps.range_sum(0, 2))  # 6  (1+2+3)
print(ps.range_sum(1, 3))  # 9  (2+3+4)
print(ps.range_sum(0, 4))  # 15 (sum all)
