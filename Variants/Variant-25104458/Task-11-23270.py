for L in range(1, 10**6):
    N = 27 + 10
    i = 1
    while 2 ** i < N:
        i += 1
    I = (L * i / 8).__ceil__()
    if I * 3548 > 12 * 1024:
        print(L)
        break