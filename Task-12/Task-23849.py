for x in range(1, 1000):
    for y in range(1, 1000):
        if x == y * 2 and x + y * 2 == 448:
            print(1000 - x - y)
