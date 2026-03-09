from string import printable
from itertools import product

ans = 0

for num in product(printable[:2], repeat = 16):
    num = "".join(num)
    if sum(num.count(i) * int(i) for i in set(num)) % 3 == 0 and num[0] != '0':
        ans += 1

print(ans)