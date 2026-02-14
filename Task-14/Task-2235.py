num = 11*15**65 + 18*15**38 - 14*15**17 + 19*15**11 + 18338
cnt = []
while num :
    r = num % 15
    if r not in cnt:
        cnt.append(r)
    num //= 15
print(len(cnt))

from string import printable

def convert(num, sys):
    num_sys = ''
    while num:
        num_sys += printable[num % sys]
        num //= sys
    return num_sys[::-1]

num = 11*15**65 + 18*15**38 - 14*15**17 + 19*15**11 + 18338
print(len(set(convert(num, 15))))