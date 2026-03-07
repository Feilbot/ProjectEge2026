for x in range(1, 27_001):
    num = 3*27**9 + 2*27**6 + 27**3 - x
    counter_0 = 0
    while num:
        if num % 27 == 0:
            counter_0 += 1
        num //= 27
    if counter_0 == 6:
        print(x)
        break