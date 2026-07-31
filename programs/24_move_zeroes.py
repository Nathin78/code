# Move all zeroes to end while maintaining order
def move_zeroes(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
    return nums

print(move_zeroes([0,1,0,3,12]))  # [1, 3, 12, 0, 0]
print(move_zeroes([0,0,1]))       # [1, 0, 0]
