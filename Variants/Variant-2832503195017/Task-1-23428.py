from itertools import permutations

graph = 'ЕД ДА АБ БВ БГ ВД'.split()
matrix = '245 136 25 15 134 2'.split()

print(*range(1, 7))
for i in permutations('АБВГДЕ'):
    i = "".join(i)
    if all(str(i.find(x) + 1) in matrix[i.find(y)] for x, y in graph):
        print(*i)

print(8 + 12)