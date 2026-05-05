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

'''from string import printable
a = printable[:16]
print(a[::2])
print(a[1::2])
print(a)
print(len(set(a)), len(a))'''

'''a = '123'
print(a[1:-1])'''

'''a = [1, 2, 3]
print("".join(a))'''

# '''with open(r'C:\Users\XYZET\Downloads\9.txt') as file:
#     data = [list(map(int, i.split())) for i in file]
#
# print(data)
# '''

# a = '1234'
# print(a[1:])

'''l = 0
r = 1
a = '12zzz2343'
sum_str = sum(int(i) for i in a[l:r] if int(i, 36) <= 9)
print(sum_str)'''

a = '**100011*'
a = a[a.count('*') - 1:-1]
print(a)