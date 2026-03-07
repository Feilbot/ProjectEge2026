from string import printable

def convert(num, sys):
    num_sys = ''
    while num:
        num_sys += printable[num % sys]
        num //= sys
    return num_sys[::-1]

num = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
print(convert(num, 25).count('0'))