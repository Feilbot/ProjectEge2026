from itertools import product
from string import printable

alphabet = printable[:12]
ans = 0

for num in product(alphabet, repeat = 7):
    if num[0] != '0':
        key_do_3_chet = False
        key_dont_3_chet = False
        key_do_3_ne_chet = False
        key_dont_3_ne_chet = False
        for i in num[::2]:
            if int(i, 12) % 3 == 0:
                key_do_3_chet = True
            else:
                key_dont_3_chet = True
        for i in num[1::2]:
            if int(i, 12) % 3 == 0:
                key_do_3_ne_chet = True
            else:
                key_dont_3_ne_chet = True
        if ((key_do_3_chet and key_dont_3_ne_chet and not key_dont_3_chet and not key_do_3_ne_chet) or
                (key_dont_3_chet and key_do_3_ne_chet and not key_do_3_chet and not key_dont_3_ne_chet)):
            ans += 1

print(ans)