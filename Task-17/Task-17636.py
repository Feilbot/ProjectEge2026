with open(r'Files/17_17636.txt') as file:
    data = [int(i) for i in file]

checker = max(i for i in data if len(str(abs(i))) == 3 and str(i)[-1] == '3')
cnt = 0
max_sum = -1_000_000

for triple in zip(data, data[1:], data[2:]):
    if any(len(str(abs(i))) == 3 and str(i)[-1] == '3' for i in triple) and sum(triple) < checker:
        cnt += 1
        max_sum = max(max_sum ,sum(triple))

print(cnt, max_sum)