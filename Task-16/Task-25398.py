from functools import lru_cache

@lru_cache(None)
def F(n):
    if n > 30:
        return F(n - 6) + 2048
    else:
        return 3 * (G(n - 5) + 13)

@lru_cache(None)
def G(n):
    if n >= 221337:
        return 2 * n + 50
    else:
        return G(n + 11) - 48


for i in range(1, 230000)[::-1]:
    G(i)
for i in range(1, 230000):
    F(i)

print(F(5078))