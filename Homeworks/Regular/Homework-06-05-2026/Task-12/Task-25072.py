for num in range(0, 30_000)[::-1]:
    line = list('*' + bin(num)[2:] + '*')
    i = len(line) - 1
    q = [1, 0]
    while True:
        if q[0]:
            if line[i] == '*':
                i -= 1
                q = [0, 1]
        elif q[1]:
            if line[i] == '*':
                break
            elif line[i] == '0':
                line[i] = '1'
                i -= 1
            else:
                line[i] = '0'
                i -= 1
    new_num = ''.join(line[1:-1])
    if int(new_num, 2) == 77:
        print(num)
        break