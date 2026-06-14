with open(r'..\..\Files\26_23208.txt') as file:
    N = int(file.readline())
    details = []
    for num, line in enumerate(file, start=1):
        grind, paint = map(int, line.split())
        details.append([grind, 'G', num])
        details.append([paint, 'P', num])

details = sorted(details)
conveyor = [0] * N

last_detail = 0

for detail in details:
    if detail[2] not in conveyor:
        if detail[1] == 'G':
            conveyor[conveyor.index(0)] = detail[2]
        else:
            conveyor[N - 1 - conveyor[::-1].index(0)] = detail[2]
        last_detail = detail[2]

print(last_detail, len(conveyor[:(conveyor.index(last_detail))]))