import sys

sys.setrecursionlimit(100_000)

def F(n):
    if n == 1:
        return 1
    elif n > 1:
        return (n + 1) * F(n - 1)

print((F(2024) - 3 * F(2023)) / F(2022))