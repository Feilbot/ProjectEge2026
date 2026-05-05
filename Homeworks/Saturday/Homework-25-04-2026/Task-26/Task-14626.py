with open(r'..\..\..\..\Files\26_14626.txt') as file:
    N = int(file.readline())
    K, M = map(int, file.readline().split())
    caves = {}
    for id in sorted(map(int, file.readline().split())):
        caves[id] = M
    weights = sorted(int(i) for i in file)

for id in caves:
    cave = caves[id]
