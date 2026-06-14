with open(r'..\Files\17_2473.txt') as file:
    data = [int(i) for i in file]

cnt = 0
min_sum = 10**10

for num in zip(data, data[1:]):
    if any(i % 7 == 0 for i in num) and any(str(i)[-1] == '3' for i in num):
        cnt += 1
        min_sum = min(min_sum, sum(num))

print(cnt, min_sum)