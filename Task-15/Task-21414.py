def f(x, y):
    return (5 < y) or (x > 32) or (x + 2*y < A)

for A in range(0, 100_000):
    if all(f(x, y) for x in range(0, 1_000) for y in range(0, 1_000)):
        print(A)
        break