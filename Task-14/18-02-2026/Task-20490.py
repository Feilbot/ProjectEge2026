ans = 0

for x in range(1, 2006):
    num = 4**163 * 5 + 12**62 - x
    count_1 = 0
    count_4 = 0
    while num:
        if num % 5 == 1:
            count_1 += 1
        elif num % 5 == 4:
            count_4 += 1
        num //= 5
    if count_1 < count_4:
        ans = x
print(ans)