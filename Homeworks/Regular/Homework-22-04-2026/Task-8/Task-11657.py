from string import printable
from itertools import product

ans = 0

for num in product(printable[:8], repeat = 6):
    num = "".join(num)
    if num[0] != '0' and '3' not in num and len(set(num)) == len(num):
        for i in printable[:8:2]:
            num = num.replace(i, '*')
        if '**' in num:
            ans += 1

print(ans)