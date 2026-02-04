def convert(sys, num):
    num_sys = ''
    while num > 0:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1]

otv = 0
maxi = 0

for N in range(1, 598):
    n = convert(4, N)
    if n[0] == '3':
        n = n.replace('1', '!')
        n = n.replace('3', '1')
        n = n.replace('!', '3')
        n = '21' + n
    else:
        n = '1' + n[1:] + '1'
    n = int(n, 4)
    if maxi < n < 598:
        maxi = n
        otv = N
print(otv)