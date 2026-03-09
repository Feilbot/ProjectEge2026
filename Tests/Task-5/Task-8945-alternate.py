from itertools import product
from string import printable

alphabet = printable[:12]
ans = 0

for num in product(alphabet, repeat = 7):
    num = "".join(num)
    if num[0] != '0':
        for i in num:
            if int(i, 12) % 3 == 0:
                num = num.replace(i, '*')
            else:
                num = num.replace(i, '=')
        if '**' not in num and '==' not in num:
            ans += 1

print(ans)