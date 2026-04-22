ans = 0

for p in range(int('A', 36) + 1, 37):
    for x in range(1, 500_001):
        if int('29A1', p) + int('47771', p) + int('12A', p) == 1_000_000 + x:
            ans = p

print(ans)