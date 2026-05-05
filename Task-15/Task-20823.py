def con(m, n):
    return m & n

def f(x):
    return (con(x, A) == 0) <= ((con(x, 77) == 0) and (con(x, 44) == 0))

for A in range(1, 100_000):
    if all(f(x) for x in range(1, 1_000)):
        print(A)
        break