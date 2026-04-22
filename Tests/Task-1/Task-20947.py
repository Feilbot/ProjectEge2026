from itertools import permutations

graph = 'АБ БГ ГИ ИЕ ЕД ДВ ВА БВ ГЖ ЖД ЖИ'.split()
matrix = '267 157 468 356 248 134 12 35'.split()

print(*range(1, 9))
for i in permutations('АБВГДЕИЖ'):
    i = "".join(i)
    if all(str(i.find(x) + 1) in matrix[i.find(y)] for x, y in graph):
        print(*i)

print('Ответ:', 24 + 15)