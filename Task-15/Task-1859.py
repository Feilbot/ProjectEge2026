def checker(x, y):
    return (2*x + y != 70) or (x < y) or (A < x)

for A in range(1, 1_000)[::-1]:
    if all(checker(x, y) for x in range(0, 1_000) for y in range(0, 1_000)):
        print(A)
        break