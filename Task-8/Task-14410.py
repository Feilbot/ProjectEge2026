from itertools import product

alphabet = sorted('АПРЕЛЬ')[::-1]

ans = 0

for pos, word in enumerate(product(alphabet, repeat = 5), start = 1):
    if pos > 387:
        break
    word = ''.join(word)
    if word[-1] == 'Ь':
        ans += 1

print(ans)