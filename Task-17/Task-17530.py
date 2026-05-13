with open(r'Files/17_17530.txt') as file:
    data = [int(i) for i in file]

checker = min(data)
min_sum = 10**10
cnt = 0

for pair in zip(data, data[1:]):
    if checker in [i % 55 for i in pair]:
        cnt += 1
        min_sum = min(min_sum, sum(pair))

print(cnt, min_sum)