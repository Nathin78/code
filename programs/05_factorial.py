# Factorial - iterative and recursive
def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)

print(factorial_iterative(5))   # 120
print(factorial_recursive(6))   # 720
