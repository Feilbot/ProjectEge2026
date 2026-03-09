from string import printable
from itertools import product

ans = 0

for num in product(printable[:12], repeat = 7):
    num = "".join(num)
    if num[0] != '0' and num.count('b') == 2:
        for i in printable[:12]:
            if int(i, 12) % 2 == 0:
                num = num.replace(i, '*')
            else:
                num = num.replace(i, '=')
        if '**' not in num and '==' not in num:
            ans += 1

print(ans)