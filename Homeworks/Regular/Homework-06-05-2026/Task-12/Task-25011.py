line = list('*' + bin(400)[2:] + '*')
i = 0
q = [1, 0]

while True:
    if q[0]:
        if line[i] == '*':
            i += 1
            q = [0, 1]
    elif q[1]:
        if line[i] == '*':
            break
        elif line[i] == '1':
            line[i] = '0'
            i += 1
        else:
            line[i] = '1'
            i += 1

print(int(''.join(line[1:-1]), 2))