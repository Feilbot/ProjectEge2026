with open(r'Files/17_9840.txt') as file:
    data = [int(i) for i in file]

checker = max(i for i in data if len(str(i)) == 4 and str(i)[-2:] == '39')

cnt = 0
max_sum = 0

for pair in zip(data, data[1:]):
    if [len(str(abs(i))) for i in pair].count(4) == 1:
        if sum(pair) ** 2 <= checker ** 2:
            cnt += 1
            max_sum = max(max_sum, sum(pair))

print(cnt, max_sum)