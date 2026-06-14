from itertools import permutations, product

def f(x, y, z, w):
    return not(y <= x) or (z <= w) or (not z)

for x in product([0, 1], repeat = 7):
    table = [
        (x[0], 0, x[1], x[2], 0),
        (0, 1, x[3], x[4], 0),
        (1, x[5], x[6], 0, 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep="")