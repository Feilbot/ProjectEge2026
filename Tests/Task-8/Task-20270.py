from itertools import product
from string import printable

cnt = 0

for num in product(printable[:7], repeat = 5):
    num = "".join(num)
    if '0' not in num[0]:
        for i in printable[:7:2]:
            num = num.replace(i, '*')
        if num.count('**') >= 2 and '***' not in num:
            cnt += 1

print(cnt)