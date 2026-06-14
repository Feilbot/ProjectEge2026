with open(r'Task-9-23440.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0

for line in data:
    if len(line) != len(set(line)):
        redacted_line = sorted(set(line))
        checker = [line.count(num) for num in redacted_line]
        if checker.count(3) == 2 and checker.count(1) == 1:
            max_num = 0
            num = 0
            for i in zip(redacted_line, checker):
                if i[1] == 3:
                    max_num = max(max_num, i[0])
                else:
                    num = i[0]
            if max_num > num:
                cnt += 1

print(cnt)