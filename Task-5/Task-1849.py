otv = 99999999999999

for N in range(1, 99999):
    n = bin(N)[2:]
    if N % 2 == 0:
        n = '1' + n + '0'
    else:
        n = '11' + n + '11'
    if 52 < int(n, 2) < otv:
        otv = int(n, 2)
print(otv)