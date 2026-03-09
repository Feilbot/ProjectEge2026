ans = []

for N in range(1, 100_000):
    n = bin(N)[2:]
    if str(int(n)).count('0') % 2 == 0:
        n = '1' + n + '1'
    else:
        n = '10' + n
    R = int(n, 2)
    if R < 100:
        ans.append(R)

print(max(ans))