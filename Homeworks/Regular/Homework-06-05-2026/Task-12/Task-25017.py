line = list('*' + '0'*151 + '*')
i = 0
q = [1, 0, 0, 0]

while True:
    if q[0]:
        i += 1
        q = [0, 1, 0, 0]
    elif q[1]:
        if line[i] == '1':
            i += 1
        elif line[i] == '0':
            i += 1
            q = [0, 0, 1, 0]
    elif q[2]:
        if line[i] == '*':
            break
        elif line[i] == '1':
            line[i] = '0'
            i += 1
            q = [0, 0, 0, 1]
        else:
            line[i] = '1'
            i += 1
            q = [0, 0, 0, 1]
    elif q[3]:
        if line[i] == '*':
            break
        elif line[i] == '1':
            i += 1
            q = [0, 0, 1, 0]
        else:
            i += 1
            q = [0, 0, 1, 0]

print(line.count('1'))