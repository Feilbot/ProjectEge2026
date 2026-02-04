otv = 0
for n in range(1, 100000):
    N = bin(n)[2:]
    if n % 3 == 0:
        N += N[(len(N)-2):]
    else:
        ost = (n % 3) * 3
        N += bin(ost)[2:]

    if int(N, 2) < 170:
        otv = int(N, 2)
print(otv)