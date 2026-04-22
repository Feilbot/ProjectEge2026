def checker(x, y):
    return ((x**2 + y**2) > (1024 - x)) or (y < -2*x + A)

for A in range(0, 100_000):
    if all(checker(x, y) for x in range(0, 1_000) for y in range(0, 1_000)):
        print(A)
        break