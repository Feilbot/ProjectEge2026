num = 15625**16 - 3125**3 * 25**19 + 625**4 - 2005

num_sys = ''
while num:
    num_sys += str(num % 5)
    num //= 5
print(str(int(num_sys[::-1])).count('0'))