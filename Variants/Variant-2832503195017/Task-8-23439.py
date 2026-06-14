from itertools import product

alphabet = sorted('АЛГОРИТМ')

for pos, word in enumerate(product(alphabet, repeat = 5), start=1):
    word = "".join(word)
    if pos % 2 == 0 and word[0] not in ['Т', 'Р'] and word.count('И') >= 2:
        ans = pos

print(ans)