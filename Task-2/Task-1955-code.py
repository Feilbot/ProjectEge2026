from itertools import product, permutations

def f(x, y, z, w):
    return (not(y <= (x == w))) and (z <= x)

for x in product([0, 1], repeat = 5):
    table = [
        (x[0], 1, 1, x[1], 1),
        (0, x[2], x[3], 0, 1),
        (x[4], 0, 1, 0, 1)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')