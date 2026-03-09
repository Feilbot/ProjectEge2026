with open(r'../../../Files/24_26077.txt') as file:
    data = file.readline()

for i in '13579':
    data = data.replace(i, '*')

data = data.split('G')

ans = 0

for line in data:
    counter_zv = line.count('*')
    if counter_zv == 45:
        ans = max(ans, len('G' + line))
    elif counter_zv > 45:
        while line.count('*') > 45:
            line = line[:line.rfind('G')]
        ans = max(ans, len('G' + line))
print(ans)