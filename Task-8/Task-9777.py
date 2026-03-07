from itertools import product

alphabet = 'ЕКМОПРТЬЮ'

ans = []
for word in product('КОМПЬЮТЕР', repeat = 5):
    if word[0] != 'Ь' and word.count('К') == 2:
        alp_word = ''
        for alp in word:
            alp_word += str(alphabet.index(alp))
        nummed = int(alp_word, 9)
        if (nummed + 1) % 2 == 1:
            ans.append(nummed + 1)

print(max(ans))