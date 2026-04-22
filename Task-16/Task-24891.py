from functools import lru_cache

@lru_cache(None)
def F(n):
    if n <= 10:
        return n
    else:
        return n - 7 + F(n - 21)

for i in range(1, 186_000):
    F(i)

print((F(185734) - F(185650)) // F(40))