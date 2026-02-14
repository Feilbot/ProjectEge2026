with open(r'..\..\..\Files\24_25361.txt') as file:
    data = file.readline()

ans = 0

for i in '02468':
    data = data.replace(i, '* *')
data = data.split()

for line in data:
    counter_F = line.count('F')
    if counter_F == 76:
        ans = max(ans, len(line))
    elif counter_F > 76:
        while line.count('F') > 76:
            line = line[:-1]
        ans = max(ans, len(line))

print(ans)