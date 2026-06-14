with open(r'..\Files\26_29234.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times = sorted(times)
computers = [0] * K
profit = [0] * K
cnt = 0

for time in times:
    for i in range(K):
        if time[0] > computers[i]:
            computers[i] = time[1]
            cnt += 1
            t = time[1] - time[0]
            profit[i] += t * (t + 1) // 2
            break

print(cnt, max(profit))