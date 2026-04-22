from functools import lru_cache

def F(n):
    if n >= 19:
        return F(n - 4) + 3580
    else:
        return 6 * (G(n - 7) - 36)

@lru_cache(None)
def G(n):
    if n >= 248045:
        return n / 20 + 28
    else:
        return G(n + 9) - 4

for i in range(250_000, 1, -1):
    G(i)

print(int(F(673)))