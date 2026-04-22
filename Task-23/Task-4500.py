from functools import lru_cache

@lru_cache(None)
def F(x, y, c):
    if x > y or x == 23 or '11' in c:
        return 0
    elif x == y:
        return 1
    else:
        return F(x + 1, y, c + '1') + F(x + 2, y, c + '0') + F(x * 2, y, c + '0')

print(F(3, 11, '') * F(11, 79, ''))