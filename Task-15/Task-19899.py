def mod(m, n):
    return m % n

def f(x):
    return (A + 2*x > 400 - A) and (mod(A, 100) + mod(120, A) > 140)

for A in range(1, 100_000):
    if all(f(x) for x in range(1, 1_000)):
        print(A)
        break