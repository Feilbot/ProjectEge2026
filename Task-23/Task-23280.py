def F(x, y):
    if x < y or x == 8:
        return 0
    elif x == y:
        return 1
    else:
        return F(x - 1, y) + F(x - 4, y) + F(x // 3, y)

print(F(19, 14) * F(14, 2))