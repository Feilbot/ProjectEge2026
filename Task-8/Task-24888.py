from itertools import product
from string import printable

ans = 0

for num in product(printable[:16], repeat = 4):
    num = "".join(num)
    if num.count('3') == 1 and num[0] != '0':
        for i in range(0, len(num) - 1):
            if num[i] == num[i + 1]:
                break
        else:
            ans += 1

print(ans)