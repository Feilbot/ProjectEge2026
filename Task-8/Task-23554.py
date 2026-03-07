from itertools import product

alphabet = 'АГИЛМОРТ'

ans = []
for word in product('АЛГОРИТМ', repeat = 5):
    if word[0] != 'А' and word[0] != 'Г' and word.count('Р') >= 2:
        alp_word = ''
        for alp in word:
            alp_word += str(alphabet.index(alp))
        nummed = int(alp_word, 8)
        if (nummed + 1) % 2 == 0:
            ans.append(nummed + 1)

print(min(ans))