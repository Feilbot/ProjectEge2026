with open(r'Files\26 (1).txt') as file:
    N = file.readline()
    data = sorted([int(i.split()[1]), int(i.split()[0])] for i in file)

ans = 0
i = data[0][0]
group = []
groups = []
for info in data:
    if i == info[0]:
        group.append(info[1])
    else:
        groups.append(group)
        group = []
    i = info[0]

for group in groups:
    if group:
        group = sorted(set(group))
        if len(group) > 1:
            maxi = 0
            for i in range(1, len(group)):
                if group[i-1] + 1 == group[i]:
                    maxi += 1
                else:
                    ans = max(ans, maxi)
print(ans)