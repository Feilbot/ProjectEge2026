import sys

sys.setrecursionlimit(100_000)

def F(n):
    if n < 7:
        return 7
    else:
        return n + 1 + F(n - 2)

print(F(2024) - F(2020))