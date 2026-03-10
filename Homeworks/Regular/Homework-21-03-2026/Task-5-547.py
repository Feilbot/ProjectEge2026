for N in range(1, 100_000):
    n = bin(N)[2:]
    for _ in range(2):
        if n.count('1') % 2 == 0:
            n += '0'
        else:
            n += '1'
    if int(n, 2) > 103:
        print(N)
        break