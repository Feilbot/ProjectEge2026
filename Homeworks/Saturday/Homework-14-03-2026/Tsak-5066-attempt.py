with open(r'..\..\..\Files\26_5066.txt') as file:
    N = file.readline()
    all_containers = sorted(int(i) for i in file)[::-1]

for i in range(len(all_containers)):
    all_containers[i] = [all_containers[i], False]

max_amount_in_one_block = 1

checked = False #For first half of task (max_in_one_block)

amount_of_blocks = 0

previous_container = all_containers[0]

while True:
    for container in all_containers:
        if previous_container[0] - container[0] >= 7 and not container[1] and not previous_container[1]:
            if not checked:
                max_amount_in_one_block += 1
            previous_container[1] = True
            previous_container = container
    checked = True

    #temporary
    print(all_containers)
    break

print(amount_of_blocks, max_amount_in_one_block)