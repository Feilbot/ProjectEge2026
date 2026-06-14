with open(r'..\..\Files\26_17643.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

middle = sum(i[1] for i in data) / N

goods = {}
for ID, price, status in data:
    if price > middle:
        if ID not in goods:
            goods[ID] = [not status, price, status]
        else:
            goods[ID][2] += status
            goods[ID][0] += (not status)

keys = sorted(goods, key=lambda x: (goods[x][0], goods[x][1], -goods[x][2]))

print(goods[keys[-1]][0] * goods[keys[-1]][1], goods[keys[-1]][-1])