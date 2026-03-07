for a in range(100_000):
    num = 3**10 + 3**7 + 3**3 + 2 - a
    count_0 = 0
    count_1 = 0
    count_2 = 0
    while num:
        if num % 3 == 0:
            count_0 += 1
        elif num % 3 == 1:
            count_1 += 1
        else:
            count_2 += 1
        num //= 3
    if count_0 == count_1 == count_2:
        print(a)
        break