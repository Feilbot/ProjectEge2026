from string import printable
from itertools import product

ans = 0
for x in 3, 5:
    for num in product(printable[:16], repeat = x):
        num = "".join(num)
        for i in printable[10:16]:
            num.replace(i, '')
        if all(num[i] > num[i + 1] for i in range(len(num) - 1)):
            ans += 1

print(ans)