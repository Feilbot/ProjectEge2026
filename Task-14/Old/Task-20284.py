from string import printable

ans = 0

for x in range(0, 43):
    x_num = x
    if x < 36:
        x = printable[x]
    else:
        x = '!'
    num_1 = f'J569{x}'[::-1]
    num_1_10 = 0
    for i in range(0, len(num_1)):
        if num_1[i] != '!':
            num_1_10 += int(num_1[i], 36) * 42**i
        else:
            num_1_10 += x_num * 42 ** i
    num_2 = f'1{x}IA'[::-1]
    num_2_10 = 0
    for i in range(0, len(num_2)):
        if num_2[i] != '!':
            num_2_10 += int(num_2[i], 36) * 42**i
        else:
            num_2_10 += x_num * 42 ** i
    if (num_1_10 + num_2_10) % 155 == 0:
        print((num_1_10 + num_2_10) // 155)
        break