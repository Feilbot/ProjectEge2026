from functools import lru_cache

@lru_cache(None)
def F(n):
    if n > 40:
        return F(n - 4) + 3020
    else:
        return 3 * (G(n - 2) - 15)

@lru_cache(None)
def G(n):
    if n >= 301208:
        return 10 * n + 50
    else:
        return G(n + 7) - 21


for i in range(1, 301300)[::-1]:
    G(i)
for i in range(1, 301300):
    F(i)

print(F(2026))