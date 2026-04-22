P = range(15, 40)
Q = range(21, 63)

ans = []

for x1 in range(15, 64):
    for x2 in range(15, 64):
        key = True
        for x in range(1, 1_000):
            f = (15 <= x <= 40) <= (((21 <= x <= 63) and (not(x1 <= x <= x2))) <= (not(15 <= x <= 40)))
            if not f:
                key = False
        if key:
            ans.append(x2 - x1 + 1)

print(min(ans))