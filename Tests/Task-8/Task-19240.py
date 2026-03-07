from itertools import product

alphabet = sorted('ЯНВАРЬ')

answer = 0

for pos, word in enumerate(product(alphabet, repeat = 5), start = 1):
    word = ''.join(word)
    if word[0] != 'Я' and word.count('Ь') <= 1 and 'ЯЯ' not in word:
        answer = pos

print(answer)