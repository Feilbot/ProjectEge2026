def f_miss_24(x, y):
    if x == y:
        return 1
    if x > y or x == 24:
        return False
    return f_miss_24(x + 1, y) + f_miss_24(x + 2, y) + f_miss_24(x + 4, y) + f_miss_24(x + 8, y)

def f_miss_32(x, y):
    if x == y:
        return 1
    if x > y or x == 32:
        return False
    return f_miss_32(x + 1, y) + f_miss_32(x + 2, y) + f_miss_32(x + 4, y) + f_miss_32(x + 8, y)

ans1 = f_miss_24(16, 32) * f_miss_24(32, 48)
ans2 = f_miss_32(16, 24) * f_miss_32(24, 48)

print(ans1 + ans2)