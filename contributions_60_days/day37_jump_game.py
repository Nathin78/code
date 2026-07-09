def can_jump(nums):
    max_reach = 0
    for i, n in enumerate(nums):
        if i > max_reach: return False
        max_reach = max(max_reach, i + n)
    return True

if __name__ == "__main__":
    print(can_jump([2, 3, 1, 1, 4]))
