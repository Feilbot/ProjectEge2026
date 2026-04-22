from itertools import product

alphabet = sorted('СДАЙЕГЭ')

ans = 0

for pos, word in enumerate(product(alphabet, repeat = 6), start=1):
    word = "".join(word)
    if 'ЕГЭ' in word:
        ans += pos

print(ans)