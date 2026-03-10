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

previous_container = all_containers[::-1][0]


largest_num_in_all_blocks = []

while all_containers:

    largest_num_in_current_block = 0
    for container in all_containers[::-1]:

        if container - previous_container >= 7:
            largest_num_in_current_block = max(largest_num_in_current_block, previous_container)
            all_containers.remove(previous_container)
            previous_container = container

    largest_num_in_all_blocks.append(largest_num_in_current_block)
    amount_of_blocks += 1
    previous_container = all_containers[::-1][0]

    if all_containers[0] - all_containers[-1] < 7:
        break



checker_for_len = 0
picked_numbers = []

for i in all_containers:
    for comparing_number in sorted(largest_num_in_all_blocks):

        if i - comparing_number >= 7 and largest_num_in_all_blocks.count(comparing_number) != picked_numbers.count(comparing_number):
            checker_for_len += 1
            picked_numbers.append(comparing_number)
            break

if checker_for_len == len(all_containers):
    print(amount_of_blocks, max_amount_in_one_block)
else:
    print(amount_of_blocks + len(all_containers) - checker_for_len, max_amount_in_one_block)