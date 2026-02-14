def convert(sys, num):
    num_sys = ''
    while num:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1]

ans = []

for N in range(3, 100_000):
    n = convert(3, N)
    if N % 3 == 0:
        n += n[-3:]
    else:
        n += convert(3, N % 3 * 3)
    if int(n, 3) <= 150:
        ans.append(N)
print(max(ans))