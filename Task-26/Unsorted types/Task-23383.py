with open(r'..\..\Files\26_23383.txt') as file:
    N = int(file.readline())
    data = [tuple(map(int, i.split())) for i in file]

data = sorted(set(data), key=lambda x: (x[1], x[0]))

cnt = 1
ans = []
for men_1, men_2 in zip(data, data[1:]):
    if men_1[1] == men_2[1] and men_2[0] - men_1[0] == 1:
        cnt += 1
    elif men_1[1] == men_2[1] and men_2[0] == men_1[0]:
        continue
    else:
        cnt = 1
    ans.append([cnt, men_1[1]])

print(*max(ans, key=lambda x: (x[0], -x[1])))