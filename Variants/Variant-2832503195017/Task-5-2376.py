for N in range(1, 10**9):
    n = bin(N)[2:]
    for _ in range(2):
        n += str(n.count('1') % 2)
    R = int(n, 2)
    if R > 60:
        print(R)
        break