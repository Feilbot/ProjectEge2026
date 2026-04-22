from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 6:
        return n
    else:
        return (3*n - 2) * F(n - 5)

for i in range(1, 20569):
    F(i)

print((F(20568) - 51702 * F(20563)) // F(20553))