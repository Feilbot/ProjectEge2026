with open(r'..\Files\26_23283.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    applies = sorted(list(map(int, i.split())) for i in file)

line = [0] * K

cnt = 0
last = 0

for client in applies:
    for i in range(K):
        if client[0] > line[i]:
            line[i] = client[1]
            cnt += 1
            last = i + 1
            break

print(cnt, last)