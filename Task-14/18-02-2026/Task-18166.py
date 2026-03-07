ans = []

for x in range(2, 2026):
    num = 5**2025 + 5**200 - x
    count_4 = 0
    while num:
        if num % 5 == 4:
            count_4 += 1
        num //= 5
    ans.append([count_4, x])
print(max(ans)[1])