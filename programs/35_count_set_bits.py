# Count set bits (1s) in binary representation
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def count_set_bits_builtin(n):
    return bin(n).count("1")

for i in range(9):
    print(f"{i}: {count_set_bits(i)} bits")
