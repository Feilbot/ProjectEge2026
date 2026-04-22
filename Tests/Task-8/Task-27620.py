from itertools import product

alphabet = sorted('ЦИТРУС')
ans = 0

for pos, word in enumerate(product(alphabet, repeat = 5), start = 1):
    word = "".join(word)
    if word.count('И') == 2 and 'ЦЦ' not in word:
        ans = pos

print(ans)