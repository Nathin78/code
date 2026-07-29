def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0: return False
    target = total // 2
    dp = {0}
    for num in nums:
        dp |= {s + num for s in dp if s + num <= target}
    return target in dp

if __name__ == "__main__":
    print(can_partition([1, 5, 11, 5]))
