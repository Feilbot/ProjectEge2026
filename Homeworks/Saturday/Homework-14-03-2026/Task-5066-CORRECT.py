with open(r'..\..\..\Files\26_5066.txt') as file:
    N = file.readline()
    containers = sorted(int(i) for i in file)[::-1]

amount_of_blocks = 0
max_amounts = []


while containers:
    max_amount_in_one_block = 1

    previous_container = containers[0]
    containers.remove(containers[0])
    for container in containers:
        if container > 0 and previous_container - container >= 7:
            previous_container = container
            containers[containers.index(previous_container)] = 0
            max_amount_in_one_block += 1
    while not all(containers):
        containers.remove(0)
    amount_of_blocks += 1
    max_amounts.append(max_amount_in_one_block)

print(amount_of_blocks, max(max_amounts))