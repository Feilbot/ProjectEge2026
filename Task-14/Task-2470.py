from string import printable

def convert(num, sys):
    num_sys = ''
    while num:
        num_sys += printable[num % sys]
        num //= sys
    return num_sys[::-1]

ans = 0

for num in range(0, 100_000):
    five_cnt = 0
    five = num
    three_cnt = 0
    three = num
    while five:
        five_cnt += 1
        five //= 5
    if five_cnt == 4:
        while three:
            three_cnt += 1
            three //= 3
        if three_cnt == 5:
            if hex(num)[-1:] == 'd':
                ans += 1

print(ans)