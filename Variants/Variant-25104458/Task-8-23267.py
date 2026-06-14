from itertools import product

alphabet = sorted('СТРОКА')
ans = 0

for pos, word in enumerate(product(alphabet, repeat = 5), start=1):
    word = "".join(word)
    if pos % 2 != 0 and word[0] not in 'АЛ' and word.count('С') == 1:
        ans = pos

print(ans)