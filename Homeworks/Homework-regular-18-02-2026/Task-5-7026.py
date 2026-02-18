ans = []

for N in range(9, 100_000):
    n = bin(N)[2:]
    if N % 2 == 0:
        n = '1' + str(n) + '00'
    else:
        n = str(n) + bin(n.count('1'))[2:]
    R = int(n, 2)
    if R > 88:
        ans.append([R, N])

print(min(ans)[1])