# GCD and LCM using Euclid algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(48, 18))   # 6
print(lcm(4, 6))     # 12
print(gcd(100, 75))  # 25
print(lcm(12, 18))   # 36
