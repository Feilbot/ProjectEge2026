def DEL(n, m):
    return n % m == 0

def f(x):
    return DEL(x, A) or (DEL(x, 23) <= (not (50 <= x <= 70)))

for A in range(1, 100_000)[::-1]:
    if all(f(x) for x in range(1, 1_000)):
        print(A)
        break