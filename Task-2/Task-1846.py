listik = []

print('a b c d')
for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                if ((not a and not b) or (b == c) or d) == 0:
                    listik.append([a, b, c, d])

#Фильтр
for i in listik:
    if sum(i) != 4 and sum(i) != 0:
        print(*i)

print('Ответ: cdba')