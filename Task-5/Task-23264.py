otv = 99999999999999

def convert(sys, num):
    num_sys = ''
    while num > 0:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1]

for N in range(1, 99999):
    n = convert(3, N)
    if N % 3 == 0:
        n += n[(len(n)-2):]
    else:
        n += convert(3, N%3*5)

    if 150 < int(n, 3) < otv:
        otv = int(n, 3)
print(otv)