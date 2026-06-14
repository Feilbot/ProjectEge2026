with open(r'..\..\Files\26_23208.txt') as file:
    N = int(file.readline())
    details = []
    for num, line in enumerate(file, start=1):
        grind, paint = map(int, line.split())
        if grind < paint:
            details.append([grind, 'G', num])
        else:
            details.append([paint, 'P', num])

details = sorted(details)
cnt_grind = sum(i[1] == 'G' for i in details[:-1])

print(details[-1][2], cnt_grind)