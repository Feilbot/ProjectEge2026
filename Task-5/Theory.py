# Стандартные системы исчисления
# Двоичная система

num = 20
print(bin(num)[2:]) # str
print(f'{num:b}')
# Восьмеричная системы
print(oct(num)[2:]) # str
print(f'{num:o}')
# Восьмеричная системы
print(hex(num)[2:]) # str
print(f'{num:x}')


# Перевод в системы 2 <= sys <= 9
def convert(sys, num):
    num_sys = ''
    while num > 0:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1]

print(convert(4, 22))

# Перевод в любую систему исчисления
from string import printable

def convert(sys, num):
    num_sys = ''
    while num > 0:
        num_sys += printable[num % sys]
        num //= sys
    return num_sys[::-1]

print(convert(14, 2322))

num_bin = 'F7QA12'

# print(sum(map(int, num_bin)))

print(sum(map(lambda x: int(x, 36), num_bin)))