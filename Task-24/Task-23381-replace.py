with open(r'..\Files\24_23381.txt') as file:
    data = file.readline()

for i in '02468':
    data = data.replace(i, '* *')

for i in '13579':
    data = data.replace(i, '!')

data = data.split()


ans = 0
for i in range(len(data)):
    if data[i].count('!') == 0:
        for let in set(data[i]):
            if data[i].count(let) == 1:
                break
        else:
            ans = max(ans, len(data[i]))
print(ans)