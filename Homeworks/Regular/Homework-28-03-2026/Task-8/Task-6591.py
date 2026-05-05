from string import printable
from itertools import product

ans = 0

for num in product(printable[:7], repeat = 5):
    num = "".join(num)
    if num.count('6') == 1 and num[0] != '0':
        if sum(num.count(i) * int(i) for i in printable[:7:2]) < sum(num.count(i) * int(i) for i in printable[1:7:2]):
            ans += 1

print(ans)