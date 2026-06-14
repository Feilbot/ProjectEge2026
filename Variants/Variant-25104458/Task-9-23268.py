with open(r'Files/task-9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0

for line in data:
    cnt += 1
    if len(set(line)) == 5:
        checker = 0
        repeated_nums = []
        umrepeated_nums = []
        for i in set(line):
            if line.count(i) == 2:
                if i not in repeated_nums:
                    checker += 1
                    repeated_nums.append(i)
            else:
                if i not in umrepeated_nums:
                    umrepeated_nums.append(i)
        if checker == 2:
            if sum(repeated_nums) / len(repeated_nums) < max(umrepeated_nums):
                print(cnt)
                break