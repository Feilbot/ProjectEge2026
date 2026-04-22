from functools import lru_cache

@lru_cache(None)
def F(x, y, c):
    c += x % 2
    if x > y or c > 4:
        return 0
    elif x == y:
        return 1
    else:
        return F(x + 2, y, c) + F(x + 3, y, c) + F(x * 2 + 1, y, c)

print(F(1, 625, 0))
