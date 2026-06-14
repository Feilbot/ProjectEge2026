def convert(num, sys):
    num_sys = ''
    while num:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1] if num_sys else '0'

ans = []

for N in range(1, 100_000):
    n = convert(N, 3)
    if N % 3 == 0:
        n += n[-2:]
    else:
        n += convert(N % 3 * 5, 3)
    R = int(n, 3)
    if R > 150:
        ans.append(R)

print(min(ans))