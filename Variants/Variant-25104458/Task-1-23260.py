from itertools import permutations
from string import ascii_uppercase

graph = 'DA AE EG GF FC CD BD BC BH HA HG'.split()
matrix = '346 348 12 127 678 15 458 257'.split()

print(*range(1, 9))
for i in permutations(ascii_uppercase[:8]):
    i = "".join(i)
    if all(str(i.find(x) + 1) in matrix[i.find(y)] for x, y in graph):
        print(*i)

print(24 + 23)