for n in range(1, 99999999999999):
    N = bin(n)[2:]
    if N.count('1') % 2 == 0:
        N += '0'
        N = '10' + N[2:]
    else:
        N += '1'
        N = '11' + N[2:]
    if int(N, 2) > 16:
        print(n)
        break