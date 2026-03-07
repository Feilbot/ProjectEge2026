from itertools import product

from string import printable

ans = 0

for number in product(printable[:15], repeat = 5):

    number = ''.join(number)

    if number.count('8') == 1 and number[0] != '0' and sum(number.count(x) for x in printable[10:15]) >= 2:
        ans += 1

print(ans)