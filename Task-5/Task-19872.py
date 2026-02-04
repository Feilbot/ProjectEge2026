def convert(sys, num):
    num_sys = ''
    while num > 0:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1]

otv = 0

for N in range(1, 1001):
    n = convert(7, N)
    if N % 2 == 0:
        n = '52' + n + '1'
    else:
        n =  n[len(n)-1] + n[1:][:len(n[1:])-1] + n[0] + '15'
    if len(str(int(n))) == 4:
        otv = N
print(otv)