from itertools import product

ans = 0

for pos, word in enumerate(product(sorted('СЕНТЯБРЬ'), repeat = 5), start = 1):
    word = "".join(word)
    if word[0] == 'Р' and 'Ь' not in word and pos % 2 == 0:
        ans = pos

print(ans)