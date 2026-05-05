line = list('*' + bin(204)[2:] + '*')
i = len(line) - 1
q = [1, 0, 0, 0]

while True:
    if q[0]:
        i -= 1
        q = [0, 1, 0, 0]
    elif q[1]:
        if line[i] == '1':
            line[i] = '0'
            i -= 1
            q = [0, 0, 1, 0]
        elif line[i] == '0':
            line[i] = '1'
            i -= 1
            q = [0, 0, 1, 0]
    elif q[2]:
        if line[i] == '*':
            break
        elif line[i] == '1':
            line[i] = '0'
            i -= 1
        else:
            line[i] = '1'
            i -= 1
            q = [0, 0, 0, 1]
    elif q[3]:
        if line[i] == '*':
            break
        elif line[i] == '1':
            i -= 1
        else:
            i -= 1
            q = [0, 0, 1, 0]

print(int(''.join(line[1:-1]), 2))