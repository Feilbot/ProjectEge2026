def convert(num, sys):
    num_sys = ''
    while num:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1]

ans = []

for N in range(1, 100_000):
    n = convert(N, 3)
    if N % 3 == 0:
        n += n[-2:]
    else:
        summ = 0
        for one_num in n:
            summ += int(one_num)
        n += convert(summ, 3)
    R = int(n, 3)
    if R > 220:
        ans.append(R)

print(min(ans))