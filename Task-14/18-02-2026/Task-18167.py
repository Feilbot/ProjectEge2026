ans = 0

for x in range(1, 10_001):
    num = 6**900 + 6**10 - x
    count_3 = 0
    count_5 = 0
    while num:
        if num % 6 == 3:
            count_3 += 1
        elif num % 6 == 5:
            count_5 += 1
        num //= 6
    if count_3 == count_5:
        ans = x
print(ans)