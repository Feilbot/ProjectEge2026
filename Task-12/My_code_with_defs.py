def q0(i):
    if num[i] == '*':
        return q1(i - 1)

def q1(i):
    if num[i] == '*':
        return q2(i + 1)
    return q1(i - 1)

def q2(i):
    if num[i] == '0':
        return q2(i + 1)
    elif num[i] == '1':
        return q3(i + 1)

def q3(i):
    if num[i] == '*':
        return q4(i + 1)
    elif num[i] == '1':
        num[i] = '0'
        return q4(i + 1)

def q4(i):
    if num[i] == '*':
        return num
    return q4(i + 1)

num = list('*' * 10 + bin(800)[2:] + '*')
i = len(num) - 1

ans = q0(i)

print(*ans, sep='')
print(int('1000100000', 2))