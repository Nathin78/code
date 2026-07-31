# Find missing number in array [0..n]
def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

def missing_number_xor(nums):
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result

print(missing_number([3,0,1]))       # 2
print(missing_number_xor([9,6,4,2,3,5,7,0,1]))  # 8
