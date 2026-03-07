from itertools import product

alphabet = 'АКОРСТ'

ans = []
for word in product('СТРОКА', repeat = 5):
    if word[0] != 'А' and word[0] != 'Л' and word.count('С') == 1:
        alp_word = ''
        for alp in word:
            alp_word += str(alphabet.index(alp))
        nummed = int(alp_word, 6)
        if (nummed + 1) % 2 == 1:
            ans.append(nummed + 1)

print(max(ans))