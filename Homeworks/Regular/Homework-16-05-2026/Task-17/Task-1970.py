with open(r'..\..\..\..\Files\17_1970.txt') as file:
    data = [int(i) for i in file]

cnt = 0
max_sum = 0
for num in zip(data, data[1:]):
    if any(i % 3 == 0 for i in num):
        cnt += 1
        max_sum = max(max_sum, sum(num))

print(cnt, max_sum)