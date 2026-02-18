from string import printable

def convert(num, sys):
    num_sys = ''
    while num:
        num_sys += printable[num % sys]
        num //= sys
    return num_sys[::-1]

num = 4*3125**2019 + 3*625**2020 - 2*125**2021 + 25**2022 - 4*5**2023 - 2024

converted_num = convert(num, 25)

ans = 0

for i in set(converted_num):
    if int(i, 25) > 10:
        ans += converted_num.count(i)

print(ans)