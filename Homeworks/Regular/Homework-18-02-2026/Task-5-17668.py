ans = []
for N in range(28, 100_000):
    n = bin(N)[2:]
    if n.count('1') % 2 == 0:
        n = '10' + n[2:] + '0'
    else:
        n = '11' + n[2:] + '1'
    ans.append(int(n, 2))
print(min(ans))