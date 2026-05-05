for N in range(1, 10 ** 6):
    L = 119
    # i = log2(N)
    i = 1 # bit
    while 2**i < N:
        i += 1
    I = (L * i / 8).__ceil__() # byte
    if I * 125300 > 23 * 1024 * 1024:
        print(N)
        break