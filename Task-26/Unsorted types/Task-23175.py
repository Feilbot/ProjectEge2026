with open(r'..\..\Files\26_2_23175.txt') as file:
    N, M = map(int, file.readline().split())
    data = [int(i) for i in file]

loads = data[:N]
containers = data[N:]

loads = sorted(loads)
containers = sorted(containers)

passed_loads = []
difference = 0
last_load = 0
ans = 0

for load in loads:
    for container in containers:
        if container >= load:
            passed_loads.append(load)
            difference = container - load
            containers.remove(container)
            break

for load in loads:
    if load not in passed_loads:
        for x in range(0, difference + 1):
            new_load = x + passed_loads[-2]
            if new_load in loads and new_load not in passed_loads:
                ans = new_load - passed_loads[-2]

print(len(passed_loads), ans)