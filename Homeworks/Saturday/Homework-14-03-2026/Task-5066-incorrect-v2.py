with open(r'..\..\..\Files\26_5066.txt') as file:
    N = file.readline()
    all_containers = sorted(int(i) for i in file)[::-1]

max_amount_in_one_block = 1
amount_of_blocks = 0

previous_container = all_containers[0]

for container in all_containers:
    if previous_container - container >= 7:
        max_amount_in_one_block += 1
        previous_container = container

for i in range(len(all_containers)):
     all_containers[i] = [all_containers[i], False]

reversed_all_containers = all_containers[::-1]

counter = 0

for i in reversed_all_containers:
    if i[0] - reversed_all_containers[0][0] < 7:
        counter += 1


a = 0


while True:
    if a <= 13:
        previous_container = reversed_all_containers[a]
    for container in reversed_all_containers:

        if container[0] - previous_container[0] >= 7:
            reversed_all_containers[reversed_all_containers.index(container)][1] = True
            reversed_all_containers[reversed_all_containers.index(previous_container)][1] = True
            previous_container = container

    a += 1
    print(reversed_all_containers)

print(reversed_all_containers)

print(amount_of_blocks, max_amount_in_one_block)