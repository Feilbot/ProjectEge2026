from itertools import permutations, product

def f(x, y, z, w):
    return (not(w <= (x == y))) and (z <= x)

for x in product([0, 1], repeat = 5):
    table = [
        (x[0], 0, 1, 0, 1),
        (0, x[1], x[2], 0, 1),
        (x[3], 1, 1, x[4], 1)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')