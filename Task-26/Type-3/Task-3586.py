with open(r'..\..\Files\26_3586.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data)[::-1]

info = []

for plant1, plant2 in zip(data, data[1:]):
    if plant1[0] == plant2[0]:
        info.append([plant1[1] - plant2[1] - 1, plant1[0]])

print(max(info)[1], max(info)[0])