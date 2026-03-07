ans = []

for x in range(1, 10_001):
    num = 7**270 + 7**170 + 7**10 - x
    count_0 = 0
    while num:
        if num % 7 == 0:
            count_0 += 1
        num //= 7
    ans.append([count_0, x])
print(max(ans)[1])