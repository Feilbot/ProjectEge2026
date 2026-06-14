with open(r'..\..\Files\26_1207.txt') as file:
    S, N = map(int, file.readline().split())
    data = [int(i) for i in file]

ans = 0
last_file = 0
max_file = 0
data = sorted(data)

for i in data:
    if S - i >= 0:
        S -= i
        ans += 1
        last_file = i

for x in range(S + 1):
    if last_file + x in data:
        max_file = last_file + x

print(ans, max_file)