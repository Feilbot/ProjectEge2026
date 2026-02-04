otv = 99999999999999

for N in range(1, 99999):
    n = bin(N)[2:]
    for _ in range(2):
        n += str(n.count('1') % 2)

    if 75 < int(n, 2) < otv:
        otv = int(n, 2)
print(otv)