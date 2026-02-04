from string import printable

def convert(sys, num):
    num_sys = ''
    while num > 0:
        num_sys += printable[num % sys]
        num //= sys
    return num_sys[::-1]

for n in range(1, 100000):
    N = convert(3, n)
    if n % 3 == 0:
        N += N[(len(N)-2):]
    else:
        ost = (n % 3) * 5
        N += convert(3, ost)[2:]

    if int(N, 3) > 133:
        print(int(N, 3))
        break