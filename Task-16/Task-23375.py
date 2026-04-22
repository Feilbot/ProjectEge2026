import sys

sys.setrecursionlimit(100_000)

def F(n):
    return G(n - 1) + G(n - 3)

def G(n):
    if n <= 9:
        return 3 * n
    else:
        return G(n - 4) + 2

print(F(42999))