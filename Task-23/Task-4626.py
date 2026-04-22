def F(x, y):
    if x < y:
        return 0
    elif x == y:
        return 1
    else:
        return F(x - 2, y) + F(x // 2, y)

print(F(28, 10) * F(10, 1))