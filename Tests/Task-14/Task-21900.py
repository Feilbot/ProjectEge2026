ans = []

for x in range(0, 2301):
    num = 7**350 + 7**150 - x
    cnt = 0
    while num:
        if num % 7 == 0:
            cnt += 1
        num //= 7
    if cnt == 200:
        ans.append(x)

print(max(ans))