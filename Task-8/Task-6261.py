from itertools import product
from string import printable

ans = 0

for num in product(printable[:8], repeat = 10):
    num = "".join(num)
    if num.count('7') == 5 and num[0] != '0':
        for i in printable[1:6:2]:
            num = num.replace(i, '*')
        if '*7' not in num and '7*' not in num and '77' not in num:
            ans += 1

print(ans)