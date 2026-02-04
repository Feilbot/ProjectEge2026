otv = 0

def convert(sys, num):
    num_sys = ''
    while num > 0:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1]

for N in range(1, 99999):
    n = convert(2, N)
    if N % 3 == 0:
        n += n[(len(n)-3):]
    else:
        n += convert(2, N%3*3)

    if int(n, 2) < 130:
        otv = N
print(otv)