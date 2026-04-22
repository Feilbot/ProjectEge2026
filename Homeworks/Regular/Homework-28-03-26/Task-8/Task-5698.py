from string import printable
from itertools import product

ans = 0

for num in product(printable[:10], repeat = 6):
    num = "".join(num)
    if sum(int(i) for i in num[:3]) == sum(int(i) for i in num[3:]):
        if all(num[:3].count(i) == 1 for i in num[:3]) and all(num[3:].count(i) == 1 for i in num[3:]):
            if True in [i in num[:3] for i in num[3:]]:
                if num[:3] != num[3:]:
                    ans += 1

print(ans)