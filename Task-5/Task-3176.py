def convert(sys, num):
    num_sys = ''
    while num:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1]

otv = 0

for N in range(1, 10_000):
    n = convert(9, N)
    for _ in range(5):
        if n.count('5') == n.count('7'):
            n += n[-1]
        else:
            counter_max = 0
            digit_max = 0
            for i in set(n):
                i_int = int(i)
                if n.count(i) >= counter_max:
                    counter_max = n.count(i)
                    digit_max = i_int
                elif n.count(i) == counter_max:
                    if i_int > digit_max:
                        digit_max = i_int
            n += str(digit_max)
    if 'bac' in hex(int(n, 9)):
        otv = N


print(otv)