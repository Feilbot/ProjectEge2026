with open(r'../../Files/26_1868.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data)[::-1]

for i in zip(data, data[1:]):
    if i[0][0] == i[1][0]:
        if i[0][1] - i[1][1] == 3:
            print(i[0][0], i[0][1] - 2)
            break