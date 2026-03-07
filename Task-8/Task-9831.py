from string import printable
from itertools import product

ans = 0
alphabet = printable[:16]

for num in product(alphabet, repeat = 3):
    num = ''.join(num)
    if num[0] != '0' and len(set(num)) == len(num):
        for x in alphabet[::2]:
            num = num.replace(x, '*')
        for x in alphabet[1::2]:
            num = num.replace(x, '!')
        if '**' not in num and '!!' not in num:
            ans += 1

print(ans)