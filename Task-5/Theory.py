def separator(number):
    print('-' * 64 + f'  {number}')

separator(1) #----------------------------------------------------------------

# Стандартные системы исчисления
num = 20
# Двоичная система
print(bin(num)[2:]) # str
print(f'{num:b}')
# Восьмеричная система
print(oct(num)[2:]) # str
print(f'{num:o}')
# Шестнадцатеричная система
print(hex(num)[2:]) # str
print(f'{num:x}')

# Перевод в 10 систему
# int(num, sys), где sys - система, из которой переводим

separator(2) #----------------------------------------------------------------

# Перевод в системы 2 <= sys <= 9
def convert(sys, num):
    num_sys = ''
    while num:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1]

print(convert(4, 22))

separator(3) #----------------------------------------------------------------

# Перевод в любую систему исчисления
from string import printable

def convert(sys, num):
    num_sys = ''
    while num:
        num_sys += printable[num % sys]
        num //= sys
    return num_sys[::-1]

print(convert(14, 2322))

separator(4) #----------------------------------------------------------------

num_bin = 'F7QA12'
# print(sum(map(int, num_bin)))
print(sum(map(lambda x: int(x, 36), num_bin)))

separator(5) #----------------------------------------------------------------

# Замена символов в строке.
# Заменить n символов слева
n = 2
new_line = 'XX'
line = 'abc123'
line = new_line + line[n:]
print(line)
# Заменить n символов справа
n = 2
new_line = 'XX'
line = 'abc123'
line = line[:-1*n] + new_line
print(line)
# Заменить все символы m в строке (все 0 поменять на 1)
line = '00110101'
line = line.replace('0', '1')
print(line)
# Заменить все символы m на n и все символы n на m (1 на 3 и 3 на 1)
line = '111333'
line = line.replace('1', '*')
line = line.replace('3', '1')
line = line.replace('*', '3')
print(line)

separator(6) #----------------------------------------------------------------

# Усложнённые варианты вопросов
# Максимальное N при максимальном R
R = 512
N = 257
ans = list()
ans.append([R, N])
print(max(ans)[1])
# Минимальное N при минимальном R
R = 512
N = 257
ans = list()
ans.append([R, N])
print(min(ans)[1])
# Минимальное N при максимальном R
R = 512
N = 257
ans = list()
ans.append([R, N])
ans = sorted(ans, key=lambda x:(-x[0], x[1]))
print(ans[0][1])
# Максимальное N при минимальном R
R = 512
N = 257
ans = list()
ans.append([R, N])
ans = sorted(ans, key=lambda x:(x[0], -x[1]))
print(ans[0][1])