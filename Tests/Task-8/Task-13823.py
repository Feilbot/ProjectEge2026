from itertools import product

ans = 0

for pos, word in enumerate(product(sorted('МИЗАНТРОП'), repeat = 5), start = 1):
    word = "".join(word)
    if pos % 2 == 0 and word[0] == 'Н' and word.count('Р') == 2:
        ans = pos

print(ans)