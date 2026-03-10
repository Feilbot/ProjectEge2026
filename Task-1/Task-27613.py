from string import ascii_uppercase
from itertools import permutations

graph = 'AD DB BE EF FA AC CD CE'.split()
matrix = '36 456 145 236 23 124'.split()

print(*range(1, 7))
for i in permutations(ascii_uppercase[:6]):
    i = "".join(i)
    if all(str(i.find(x) + 1) in matrix[i.find(y)] for x, y in graph):
        print(*i)