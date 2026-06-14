with open(r'..\..\Files\26_23570.txt') as file:
    N, K = map(int, file.readline().split())
    file = file.readlines()
    dachas = [int(i) for i in file[:N]]
    vehicles = [list(map(int, i.split())) for i in file[N:]]

dachas = sorted(dachas)
vehicles = sorted(vehicles, key=lambda x: (x[1], x[0]))

able = []

for d in dachas:
    for v in vehicles.copy():
        if v[0] >= d:
            able.append([v[1], v[0]])
            break
        else:
            vehicles.remove(v)

print(sum(i[0] for i in able), able[-1][1])