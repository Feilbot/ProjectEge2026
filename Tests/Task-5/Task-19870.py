def convert(num, sys):
    num_sys = ''
    while num:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1] if num_sys else '0'

ans = []

for N in range(0, 100_000):
    n = convert(N, 4)
    if N % 2 == 0:
        n = '12' + n + convert(int(n[-1]) * 3, 4)
    else:
        n = '13' + n + '21'
    R = int(n, 4)
    if R > 50:
        ans.append(R)
print(min(ans))