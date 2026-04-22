def F(x, y, c1, c2, c3):
    if x > y:
        return 0
    elif x == y and c1 <= 4 and c2 >= 2 and c3 == 5:
        return 1
    else:
        return F(x * 5, y, c1 + 1, c2, c3) + F(x * 3, y, c1, c2 + 1, c3) + F(x + 45, y, c1, c2, c3 + 1)

print(F(1, 2970, 0, 0, 0))