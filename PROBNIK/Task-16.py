from functools import lru_cache

def F(n):
    return 3 * (G(n - 2) + 5)

@lru_cache(None)
def G(n):
    if n < 8:
        return 3 * n
    else:
        return G(n - 3) + 2

for i in range(10_000):
    G(i)

print(F(12_345))