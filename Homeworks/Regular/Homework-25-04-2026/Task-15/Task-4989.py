def DEL(n, m):
    return n % m == 0


def f(x):
    return (20 <= x <= 80) <= (DEL(x, 17) <= (A1 <= x <= A2))


ans = []

for A1 in range(1, 1_000):
    for A2 in range(A1 + 1, 1_000):
        if all(f(x) for x in range(1, 1_000)):
            ans.append(A2 - A1)

print(min(ans))
