from itertools import product
from string import printable

ans = 0

for num in product(printable[:7], repeat = 6):
    num = "".join(num)
    if num[0] != '0' and sum(num.count(i) for i in printable[:7:2]) == sum(num.count(i) for i in printable[1:7:2]) and int(num[-1]) >= 4:
        ans += 1

print(ans)