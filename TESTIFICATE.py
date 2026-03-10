"""x = '55'
a = f'1{x}q2'
for i in a:
    print(i)
from string import printable
print(printable.index('!'))
print(printable[36])
print([str(x)])
print(int(str(x), 36))"""

'''line = '12345678'
print(line[:-1])'''

'''a = '123443121'
b = list(map(int, a))
print(b)

def convert(num, sys):
    num_sys = ''
    while num:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1]

a = 0
print(convert(a, 4))'''

from string import printable
a = printable[:16]
print(a[::2])
print(a[1::2])
print(a)
print(len(set(a)), len(a))