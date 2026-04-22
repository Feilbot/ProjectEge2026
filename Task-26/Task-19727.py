with open(r'..\Files\26.2_19727.txt') as file:
    M, N = map(int, file.readline().split())
    cans = sorted(int(i) for i in file)

cnt = 0
last_can = 0

for can in cans:
    if M - can >= 0:
        cnt += 1
        M -= can
        last_can = can
    else:
        break

print(cnt, len([i for i in cans if i > M + last_can]))