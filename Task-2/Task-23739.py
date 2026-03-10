from itertools import product, permutations

def f(x, y, z, w):
    return (x or y) and (not (y == z)) and (not w)

for x1, x2, x3, x4 in product([0, 1], repeat = 4):
    table = [
        (1, x1, 1, x2, 1),
        (0, 1, x3, 0, 1),
        (x4, 1, 1, 0, 1)
    ]

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')