num = list('*' * 10 + bin(800)[2:] + '*')

i = len(num) - 1

q = [1, 0, 0, 0, 0]

while True:
    if q[0]:
        if num[i] == '*':
            i -= 1
            q = [0, 1, 0, 0, 0]
    elif q[1]:
        if num[i] == '*':
            i += 1
            q = [0, 0, 1, 0, 0]
        elif num[i] == '0':
            num[i] = '0'
            i -= 1
        else:
            num[i] = '1'
            i -= 1
    elif q[2]:
        if num[i] == '0':
            num[i] = '0'
            i += 1
        elif num[i] == '1':
            num[i] = '1'
            i += 1
            q = [0, 0, 0, 1, 0]
    elif q[3]:
        if num[i] == '*':
            num[i] = '*'
            i += 1
            q = [0, 0, 0, 0, 1]
        elif num[i] == '0':
            num[i] = '0'
            i += 1
        else:
            num[i] = '0'
            i += 1
            q = [0, 0, 0, 0, 1]
    elif q[4]:
        if num[i] == '*':
            break
        elif num[i] == '0':
            num[i] = '0'
            i += 1
        else:
            num[i] = '1'
            i += 1

print(*num, sep='')
print(int('1000100000', 2))