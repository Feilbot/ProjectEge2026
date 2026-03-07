ans = 0

for x in range(1, 2031):
    num = 7**170 + 7**100 - x
    count_0 = 0
    while num:
        if num % 7 == 0:
            count_0 += 1
        num //= 7
    if count_0 == 71:
        ans = x
print(ans)