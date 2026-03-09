from math import log2

ans = 0
for N in range(1, 10 ** 6):
    L = 10 + 25
    i = log2(N).__ceil__()
    I = ((L * i / 8) + 48).__ceil__()
    if 1536 * I <= 120 * 1024:
        ans = N

print(ans)