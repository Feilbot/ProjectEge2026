def f(x, y):
    return (x * y < A) or (x < y) or (9 < x)

for A in range(0, 1_000):
    if all(f(x, y) for x in range(0, 1_000) for y in range(0, 1_000)):
        print(A)
        break