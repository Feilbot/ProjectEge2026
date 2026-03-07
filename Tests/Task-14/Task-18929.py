ans = 0

for x in range(0, 2025):
    num = 9**2024 + 9**1987 - x
    cnt = 0
    while num:
        if num % 9 == 8:
            cnt += 1
        num //= 9
    if cnt == 1984:
        ans = x
print(ans)