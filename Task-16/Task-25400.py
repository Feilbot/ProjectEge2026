from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 31054:
        return F(n + 4) + 3020
    else:
        return 3 * (G(n - 2) - 15)

@lru_cache(None)
def G(n):
    if n >= 28:
        return G(n - 5) - 15
    else:
        return 3 * n - 4


for i in range(1, 32000):
    G(i)
for i in range(32000, 1, -1):
    F(i)

print(F(15))