with open(r'Files\17_23376.txt') as file:
    data = [int(i) for i in file]

checker = max(i for i in data if len(str(abs(i))) == 5 and str(i)[-2:] == '37') ** 2
max_sum = 0
cnt = 0

for num in zip(data, data[1:]):
    if sum(len(str(abs(i))) == 5 for i in num) == 1 and sum(num)**2 > checker:
        cnt += 1
        max_sum = max(max_sum, sum(num))

print(cnt, max_sum)