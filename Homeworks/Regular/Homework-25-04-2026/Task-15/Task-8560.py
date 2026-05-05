def f(x, y, z):
    return (2*x + y != 136) or (z * y < 100) or (A**2 >= x + y)

for A in range(10_000):
    if all(f(x, y, z) for x in range(0, 1_000) for y in range(0, 1_000) for z in range(0, 1_000)):
        print(A)
        break