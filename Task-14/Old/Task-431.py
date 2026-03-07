def convert(num, sys):
    num_sys = ''
    while num:
        num_sys += str(num % sys)
        num //= sys
    return num_sys

for x in range(0, 100_000):
    num_m = 3*7**(x+1) + 13*7**(x+2) + 31*7**(3*x) + 1*7**(2*x)
    if sum(map(lambda l: int(l, 36), convert(num_m, 7))) == 18:
        print(x)
        break