def convert_2(num, sys):
    num_sys = 0
    for i in range(len(num)):
        num_sys += int(num[i], 36) * sys ** (len(num) - i - 1)
    return num_sys

for x in range(42):
    num_1 = convert_2(list('J569') + [str(x)], 42)
    num_2 = convert_2(list('1') + [str(x)] + list('IA'), 42)
    num = num_1 + num_2
    if num % 155 == 0:
        print(num//155)
        break