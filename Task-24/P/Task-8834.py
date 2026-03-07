with open(r'..\..\Files_P\24_8834.txt') as file:
    data = file.readline()

ans = 100_000

data = data.split('.')

for line in data:
    if line.count('A') == 98:
        while line.count('A') == 98:
            line = line[1:]
        ans = min(ans, len(line + '.'))
print(ans)