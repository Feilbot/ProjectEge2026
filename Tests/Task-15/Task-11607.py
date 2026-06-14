def DEL(n, m):
    return n % m == 0
def F(x):
    return not(DEL(x, 263) <= DEL(x, A)) and DEL(x, 71)

ans = 0

for A in range(1, 50_000):
    if all((not F(x)) for x in range(1, 30_000)):
        ans = A

print(ans)