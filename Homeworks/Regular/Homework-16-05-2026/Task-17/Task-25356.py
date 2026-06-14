with open(r'..\..\..\..\Files\17_25356.txt') as file:
    data = [int(i) for i in file]

cnt = 0
max_sum = 0

checker = max(i for i in data if str(i)[-2:] == '30')

for num in zip(data, data[1:], data[2:]):
    if sum(num) > checker and all(len(str(abs(i))) != 4 for i in num):
        cnt += 1
        max_sum = max(max_sum, sum(num))

print(cnt, max_sum)