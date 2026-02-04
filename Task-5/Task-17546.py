otv = 0

for n in range(1, 13):
    N = bin(n)[2:]
    if N.count('1') % 2 == 0:
        N = '10' + N[2:]
    else:
        N = '1' + N + '01'
    if int(N, 2) > otv:
        otv = int(N, 2)

print(int(N, 2))