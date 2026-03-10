from string import ascii_uppercase
from itertools import permutations

graph = 'AE EH HG GC CF FA ED HB GB FD BD'.split()
matrix = '23 168 158 578 347 27 456 234'.split()

print(*range(1, 9))
for i in permutations(ascii_uppercase[:8]):
    i = "".join(i)
    if all(str(i.find(x) + 1) in matrix[i.find(y)] for x, y in graph):
        print(*i)

print('Ответ:', 14 + 17)