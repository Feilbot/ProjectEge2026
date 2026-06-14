with open(r'..\..\Files\26_21598.txt') as file:
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times = sorted(times)

timeline = [0] * (24 * 60 + 1)

for time in times:
    for i in range(time[0], time[1] + 1):
        timeline[i] += 1

ans = 0
cnt = 0
changed = []

for i in range(1, 24 * 60):
    if timeline[i - 1] == timeline[i] == timeline[i + 1] != 0:
        cnt += 1
    elif timeline[i] != timeline[i + 1]:
        changed.append(i)
        cnt = 0
    ans = max(ans, cnt)

print(changed[-2], ans)