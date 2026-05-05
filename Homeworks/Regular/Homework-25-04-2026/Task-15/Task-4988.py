def DEL(n, m):
    return n % m == 0


def f(x):
    return not (DEL(x, 12) and (70 <= x <= 80) and (not DEL(x, A)))


ans = []

for A in range(1, 1_000):
    if all(f(x) for x in range(1, 1_000)):
        ans.append(A)

print(len(set(ans)))
