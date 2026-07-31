# Check if a number is a power of two using bit manipulation
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

for i in range(0, 20):
    if is_power_of_two(i):
        print(i, end=" ")  # 1 2 4 8 16
print()
