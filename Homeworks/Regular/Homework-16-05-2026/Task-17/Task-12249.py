with open(r'..\..\..\..\Files\17_12249.txt') as file:
    data = [int(i) for i in file]

cnt = 0
max_sum = 0
checker = max(i for i in data if len(str(i)) == 5 and str(i)[-1] == '3')

for num in zip(data, data[1:], data[2:]):
    if any(str(i)[-1] == '3' for i in num) and sum(num) <= checker:
        cnt += 1
        max_sum = max(max_sum, sum(num))

print(cnt, max_sum)