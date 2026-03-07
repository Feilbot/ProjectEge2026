from itertools import product

alphabet = 'ЕИОРТЯ'

ans = []
for word in product('ТЕОРИЯ', repeat = 6):
    if word[0] != 'Р' and word[0] != 'Т' and word[0] != 'Я' and word.count('И') >= 2:
        alp_word = ''
        for alp in word:
            alp_word += str(alphabet.index(alp))
        nummed = int(alp_word, 6)
        if (nummed + 1) % 2 == 1:
            ans.append(nummed + 1)

print(max(ans))