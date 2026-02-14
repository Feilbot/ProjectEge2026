for N in range(1, 100_000):
    n = bin(N)[2:]
    if N % 5 == 0:
        n += '11'
    else:
        n += bin(N//5)[2:]
    if int(n, 2) > 896 and N % 2 == 0:
        print(N)
        break