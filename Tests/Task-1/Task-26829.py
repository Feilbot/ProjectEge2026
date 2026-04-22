from itertools import permutations

graph = 'ГБ БЖ ЖЕ ЕВ ВД ДГ ГК БК КА АЕ АД'.split()
matrix = '248 137 268 15 467 357 256 13'.split()

print(*range(1, 9))
for i in permutations('АБВГДЕЖК'):
    i = "".join(i)
    if all(str(i.find(x) + 1) in matrix[i.find(y)] for x, y in graph):
        print(*i)

print('Ответ:', 43)