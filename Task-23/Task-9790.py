def F(x, y):
    if x < y or x == 9 or x == 16:
        return 0
    elif x == y:
        return 1
    else:
        return F(x - 1, y) + F(x - 2, y) + F(x // 3, y)

print(F(19, 3))