with open(r'Files\26 (1).txt') as file:
    N = file.readline()
    info = sorted([int(i.split()[0]), int(i.split()[1])] for i in file)

with open(r'Files\26 (1).txt') as file:
    N = file.readline()
    points = sorted(set(int(i.split()[1]) for i in file))

ans = 0

groups = []
for point in points:
    group = []
    for data in info:
        if data[1] == point:
            group.append(data[0])
    group = sorted(set(group))
    if len(group) >= 2:
        groups.append(group)

for one_group in groups:
    key = True
    for i in range(1, len(one_group)):
        if one_group[i-1] + 1 != one_group[i]:
            key = False
    if key:
        ans = max(ans, len(one_group))

print(ans)