# Container with Most Water (two pointers)
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        water = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

print(max_area([1,8,6,2,5,4,8,3,7]))  # 49
print(max_area([1,1]))                 # 1
