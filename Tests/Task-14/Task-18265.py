ans = 0

for p in range(int(max('RTNK'), 36) + 1, 37):
    for s in range(int('B', 36) + 1, 35):
        if int('R4', p - 1) + int('B0', s + 2) + int('T3NK4', p) == 23593399:
            print(p * s)
            break