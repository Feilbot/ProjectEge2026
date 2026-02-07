ans = []

for N in range(1, 100_000):
    n = bin(N)[2:]
    if N % 2 == 0:
        n = n.replace('0', '1')
    else:
        n = '1' + n[1:].replace('1', '00')
    R = int(n, 2)
    if R <= 600:
        ans.append([R, N])

print(max(ans)[1])