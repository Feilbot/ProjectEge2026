with open(r'Files\17_23757.txt') as file:
    data = [int(i) for i in file]

cnt = 0
checker = min(i for i in data if len(str(i)) == 2)
max_sum = 0

for num in zip(data, data[1:]):
    if sum(len(str(i)) == 2 for i in num) == 1 and sum(num) % checker == 0:
        cnt += 1
        max_sum = max(max_sum, sum(num))

print(cnt, max_sum)