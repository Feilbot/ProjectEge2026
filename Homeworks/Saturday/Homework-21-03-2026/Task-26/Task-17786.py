with open(r'..\..\..\..\Files\26_17786.txt') as file:
    info = file.readline()
    watermelons = sorted(set(int(i) for i in file if 7000 <= int(i) <= 12000))[::-1]

V = int(info.split()[1]) * 1000

cnt = 0
ans = 0

for watermelon in watermelons:
    if V - watermelon >= 0:
        V -= watermelon
        cnt += 1
        ans = watermelon

print(cnt, ans)