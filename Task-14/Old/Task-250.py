ans = 0
for N in range(0, 41):
    if bin(N)[2:][-4:] == '1011':
        ans = N
print(ans)