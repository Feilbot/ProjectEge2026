with open(r'..\..\Files\26_24.txt') as file:
    S, N = map(int, file.readline().split())
    data = [int(i) for i in file]

data = sorted(data)
max_user_file = 0

ans = 0
for i in data:
    S -= i
    if S < 0:
        S += i
        break
    ans += 1
    for x in range(0, 20):
        if S + i - x in data:
            max_user_file = S + i - x
            break

print(ans, max_user_file)