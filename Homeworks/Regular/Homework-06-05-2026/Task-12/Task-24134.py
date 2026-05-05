line = list('*' + '0' * 1000 + '*')
line = list('*' + '0' * 901 + '1' * 99 + '*')
line = list('*' + '0' * 901 + '1' + '01' * 49 + '*')
i = len(line) - 1
q = [1, 0]

while True:
    if q[0]:
        if line[i] == '*':
            i -= 1
            q = [0, 1]
        elif line[i] == '1':
            line[i] = '0'
            i -= 1
        else:
            i -= 1
            q = [0, 1]
    elif q[1]:
        if line[i] == '*':
            break
        elif line[i] == '1':
            line[i] = '0'
            i -= 1
            q = [1, 0]
        else:
            line[i] = '1'
            i -= 1

print(line.count('0'), ''.join(line))
print(101 + 49)