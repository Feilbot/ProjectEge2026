with open(r'Files/17_17558.txt') as file:
    data = [int(i) for i in file]

checker = len([i for i in data if i % 32 == 0])
cnt = 0
max_sum = -1_000_000

for pair in zip(data, data[1:]):
    if any(True for i in pair if i < 0) and sum(pair) < checker:
        cnt += 1
        max_sum = max(max_sum, sum(pair))

print(cnt, max_sum)