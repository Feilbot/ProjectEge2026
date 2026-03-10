from itertools import permutations
from string import ascii_uppercase

graph = 'FG GE EA AH HB BF HC FC CA DG DE'.split()
matrix = '247 148 467 123 68 358 12 256'.split()

print(*range(1, 9))
for i in permutations(ascii_uppercase[:8]):
    i = "".join(i)
    if all(str(i.find(x) + 1) in matrix[i.find(y)] for x, y in graph):
        print(*i)
