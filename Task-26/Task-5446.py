with open(r'..\Files\26_5446.txt') as file:
    N = int(file.readline())
    pipes = sorted([tuple(map(int, i.split())) for i in file], key = lambda x: -x[0] + 2 * x[1])

all_pipes = [pipes[0]]

for pipe in pipes:
    if all_pipes[-1][0] - 2 * all_pipes[-1][1] - pipe[0] >= 3:
        all_pipes += [pipe]

all_pipes = all_pipes[:-1]

for pipe in sorted(pipes, key = lambda x: -x[0]):
    if all_pipes[-1][0] - 2 * all_pipes[-1][1] - pipe[0] >= 3:
        all_pipes += [pipe]
        break

print(len(all_pipes), all_pipes[-1][0])