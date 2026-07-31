# Two Pointers - pair with given sum in sorted array
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []

print(two_sum_sorted([1, 2, 3, 4, 6], 6))   # [1, 3]
print(two_sum_sorted([2, 5, 9, 11], 11))     # [0, 2]
