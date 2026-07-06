def rob(nums):
    prev1 = prev2 = 0
    for n in nums:
        temp = max(prev1, prev2 + n)
        prev2 = prev1
        prev1 = temp
    return prev1

if __name__ == "__main__":
    print(rob([2, 7, 9, 3, 1]))
