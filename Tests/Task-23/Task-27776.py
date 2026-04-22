def F(x, y):
    if x == y:
        return 1
    elif x < y:
        return 0
    else:
        return F(x - 1, y) + F(x // 2, y)

print(F(40, 16) * F(16, 6))