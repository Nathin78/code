# Rotate array to the right by k steps
def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

def rotate_reverse(nums, k):
    k %= len(nums)
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums

print(rotate([1,2,3,4,5,6,7], 3))        # [5,6,7,1,2,3,4]
print(rotate_reverse([1,2,3,4,5,6,7],3)) # [5,6,7,1,2,3,4]
