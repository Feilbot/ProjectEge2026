def convert(num, sys):
    num_sys = ''
    while num:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1]

for N in range(1, 100_000)[::-1]:
    n = convert(N, 3)
    if N % 3 == 0:
        n = '1' + n + '02'
    else:
        n += convert((N % 3) * 4, 3)
    if int(n, 3) < 199:
        print(N)
        break