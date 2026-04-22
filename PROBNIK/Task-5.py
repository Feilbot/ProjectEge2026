def convert(num, sys):
    num_sys = ""
    while num:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1]

ans = []

for N in range(1, 100_000):
    n = convert(N, 4)
    if N % 4 == 0:
        n += n[:2]
    else:
        n += convert((N % 4) * 4, 4)
    R = int(n, 4)
    if R > 291:
        ans.append(R)

print(min(ans))