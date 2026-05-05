def cif(x, y):
    return str(x)[-1] == str(y)[-1]

def f(x):
    return ((not cif(x, 5)) and cif(x, 4)) <= (x > A - 11)

for A in range(1, 100_000)[::-1]:
    if all(f(x) for x in range(1, 1_000)):
        print(A)
        break