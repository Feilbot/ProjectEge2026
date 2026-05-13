with open(r'Files/17_9786.txt') as file:
    data = [int(i) for i in file]

checker = max(i for i in data if str(i)[-2:] == '25')
max_sum = 0
cnt = 0

for num in zip(data, data[1:], data[2:]):
    if [len(str(abs(i))) for i in num].count(4) <= 2:
        if sum(num) <= checker:
            cnt += 1
            max_sum = max(max_sum, sum(num))

print(cnt, max_sum)