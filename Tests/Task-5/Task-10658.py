def convert(num, sys):
    num_sys = ''
    while num:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1]

ans = []

for N in range(11, 100_000):
    n = convert(N, 3)
    if n.count('0') + n.count('2') > n.count('1'):
        n = '22' + n
    else:
        n = '11' + n
    R = int(n, 3)
    if R > 100:
        ans.append(R)

print(min(ans))