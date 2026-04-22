from itertools import product

ans = []

for pos, word in enumerate(product(sorted('МЫСЛЬ'), repeat = 5), start = 1):
    word = "".join(word)
    if word[:2] == 'ЫЫ':
        ans.append(pos)

print(ans[-2])