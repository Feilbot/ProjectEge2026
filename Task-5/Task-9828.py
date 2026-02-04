from string import printable

def convert(sys, num):
    num_sys = ''
    while num > 0:
        num_sys += printable[num % sys]
        num //= sys
    return num_sys[::-1]

otv = 0

for n in range(1, 100000):
    N = convert(3, n)
    if n % 3 == 0:
        N = '1' + N + '02'
    else:
        ost = (n % 3) * 4
        N += convert(3, ost)[2:]

    if int(N, 3) < 199:
        otv = n
print(otv)