with open(r'..\Files\26_20815.txt') as file:
    N, K = map(int, file.readline().split())
    astronauts = [[sum(map(int, i.split()[1:4])) + int(i.split()[4]), int(i.split()[4]), int(i.split()[0])] for i in file]

astronauts = sorted(astronauts, key=lambda x: (-x[0], -x[1], x[2]))

passed = astronauts[:K]
rejected = astronauts[K:]
half_pass = passed[-1][0]

# check:
print(passed[-1], rejected[0])
#-----

print([astronaut[-1] for astronaut in passed[::-1] if astronaut[0] != half_pass][0])
print(len([astronaut for astronaut in astronauts if astronaut[0] == half_pass]))