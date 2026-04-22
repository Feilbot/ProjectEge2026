from string import printable
from itertools import product

ans = 0

for num in product(printable[:7], repeat = 7):
    num = "".join(num)
    if all(num[0] != i for i in '035') and not(all(i in num for i in ('22', '44'))):
        ans += 1

print(ans)