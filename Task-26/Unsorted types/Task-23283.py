with open(r'..\..\Files\26_23283.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data)

timeline = [0] * K
ans = 0
last_window = 0

for client in data:
    for i in range(0, K):
        if timeline[i] < client[0]:
            timeline[i] = client[1]
            ans += 1
            last_window = i + 1
            break

print(ans, last_window)