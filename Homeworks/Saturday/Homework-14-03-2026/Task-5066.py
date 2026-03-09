with open(r'..\..\..\Files\26_5066.txt') as file:
    N = file.readline()
    containers = sorted(set(int(i) for i in file))[::-1]

max_amount_in_one_block = 1
amount_of_blocks = 0

previous_container = containers[0]

while len(containers) > len([56, 54, 53, 52, 51, 50]):
    for container in containers:
        if previous_container - container >= 7:
            if amount_of_blocks == 0:
                max_amount_in_one_block += 1
            containers.remove(previous_container)
            previous_container = container
    amount_of_blocks += 1
    previous_container = containers[0]

amount_of_blocks += len([56, 54, 53, 52, 51, 50])

print(amount_of_blocks, max_amount_in_one_block)