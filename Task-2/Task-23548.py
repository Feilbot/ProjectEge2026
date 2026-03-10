from itertools import product, permutations

def f(x, y, z, w):
    return ((x or y) <= z) or (y == w) or z

for x in product([0, 1], repeat = 4):
    table = [
        (0, 1, x[0], x[1])
    ]