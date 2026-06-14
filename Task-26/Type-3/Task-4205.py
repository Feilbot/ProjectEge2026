with open(r'..\..\Files\26_4205.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data)[::-1]
max_line = -1

for tree1, tree2 in zip(data, data[1:]):
    if tree1[0] == tree2[0]:
        if tree1[1] - tree2[1] == 14:
            print(tree2[0], tree2[1] + 1)
            break