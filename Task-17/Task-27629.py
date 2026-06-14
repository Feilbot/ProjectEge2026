with open(r'Files\17_27629.txt') as file:
    data = [int(i) for i in file]

cnt = 0
max_sum = 0
checker = max(i for i in data if len(str(abs(i))) == 4 and str(i)[-2:] == '43')

for num in zip(data, data[1:]):
    if any(len(str(abs(i))) == 4 for i in num) and sum(num)**2 < checker**2:
        cnt += 1
        max_sum = max(max_sum, sum(num)**2)

print(cnt, max_sum)