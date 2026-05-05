from functools import lru_cache

@lru_cache(None)
def F(n):
    if n >= 10 and n % 2 == 0:
        return 3 * n - 1 + F(n - 3)
    elif n >= 10 and n % 2 != 0:
        return 5 * n + 2 + F(n - 4)
    else:
        return n

for i in range(4445):
    F(i)

print(F(4445) - F(4444))