from string import printable

from itertools import product

ans = 0

for num in product(printable[:8], repeat = 5):
    num = ''.join(num)
    if num[0] not in '01357' and num[-1] not in '26' and num.count('7') <= 2:
        ans += 1

print(ans)