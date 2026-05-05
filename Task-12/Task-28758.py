num = list('*' + '2' * 323 + '0' * 115 + '1' * 562 + '*' * 10)

i = 0

q = [1, 0]

while True:
    if q[0]:
        if num[i] == '*':
            i += 1
            q = [0, 1]
    elif q[1]:
        if num[i] == '0':
            num[i] = '2'
            i += 1
        elif num[i] == '1':
            num[i] = '0'
            break
        elif num[i] == '2':
            num[i] = '1'
            i += 1

print(sum(int(i) for i in num if i != '*'))