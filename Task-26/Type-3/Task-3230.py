with open(r'..\..\Files\26_3230.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data)[::-1]

pairs = []

for sapling1, sapling2 in zip(data, data[1:]):
    if sapling1[0] == sapling2[0]:
        if sapling1[1] - sapling2[1] == 12:
            pairs.append([sapling1, sapling2])

print(pairs[0][0][0], pairs[0][1][1] + 1)