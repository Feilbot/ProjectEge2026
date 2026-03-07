with open(r'..\..\Files_P\24_8702.txt') as file:
    data = file.readline()

data = data.replace('.A', ' +')
data = data.split()


K = 0
ans = []
key = False
counter = 0

for line in data:
    if line[0] == '+':
        K += 1
        key = True
    if key:
        counter += len(line) + 1
    if K >= 600 and line[-1] == '.':
        ans.append(counter)
        counter = 0
        K = 0

print(min(ans))