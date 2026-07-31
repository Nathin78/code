# Fibonacci sequence - iterative and recursive
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

for i in range(10):
    print(fib_iterative(i), end=" ")  # 0 1 1 2 3 5 8 13 21 34
