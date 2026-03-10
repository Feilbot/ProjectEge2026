from itertools import product, permutations

def f(x, y, z, w):
    return (not(x <= z)) or (y == w) or y

for x in product([0, 1], repeat = 7):
    table = [
        (1, 0, x[0], x[1], 0),
        (x[2], 1, 0, x[3], 0),
        (0, x[4], x[5], x[6], 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')