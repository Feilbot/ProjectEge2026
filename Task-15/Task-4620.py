def f(x, y):
    return (x + y <= 22) or (y <= x - 6) or (y >= A)

for A in range(0, 1_000)[::-1]:
    if all(f(x, y) for x in range(0, 1_000) for y in range(1_000)):
        print(A)
        break