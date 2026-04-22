def M(num):
    min_del = 0
    for x in range(12, num//2 + 1):
        if num % x == 0 and str(x)[-2:] == '11':
            min_del = x
    return min_del
cnt = 0

for num in range(1_350_051, 100_000_000):
    min_del = M(num)
    if min_del:
        print(num, min_del)
        cnt += 1
    if cnt == 5:
        break