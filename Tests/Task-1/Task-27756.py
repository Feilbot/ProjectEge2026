from string import ascii_uppercase
from itertools import permutations

graph = 'AE EG GF FB BH HA ED GD FC CH CA'.split()
matrix = '247 148 467 123 68 358 13 256'.split()

print(*range(1, 9))
for i in permutations(ascii_uppercase[:8]):
    i = "".join(i)
    if all(str(i.find(x) + 1) in matrix[i.find(y)] for x, y in graph):
        print(*i)

print(37 + 28)