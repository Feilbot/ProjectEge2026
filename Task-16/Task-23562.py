import sys

sys.setrecursionlimit(100_000)

def F(n):
    return G(n - 1)

def G(n):
    if n <= 9:
        return 3 * n
    else:
        return G(n - 2) + 1

print(F(47995))