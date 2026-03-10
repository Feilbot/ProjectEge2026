from string import ascii_uppercase
from itertools import permutations

graph = 'AC CD AG GD AD DB DE BF FE'.split()
matrix = '37 57 147 37 26 57 12346'.split()

print(*range(1, 8))
for i in permutations(ascii_uppercase[:7]):
    i = "".join(i)
    if all(str(i.find(x) + 1) in matrix[i.find(y)] for x, y in graph):
        print(*i)

print('Ответ:', 26)