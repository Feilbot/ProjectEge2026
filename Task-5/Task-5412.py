from string import printable

def convert(sys, num):
    num_sys = ''
    while num > 0:
        num_sys += printable[num % sys]
        num //= sys
    return num_sys[::-1]

otv = 0

for N in range(1, 100_000):
    n = convert(16, N)
    if n.count('b') % 2 == 0:
        n = '1' + n
    else:
        n += '1'
    if len(str(int(n, 16))) == 2:
        otv += 1
print(otv)