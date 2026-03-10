from itertools import product, permutations

def f(x, y, z, w):
    return (x and not y) or (y == z) or not w

for x1, x2, x3, x4 in product([0, 1], repeat = 4):
    table = [
        (x1, x2, 0, 0, 0),
        (1, 0, x3, 0, 0),
        (1, 0, 1, x4, 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')