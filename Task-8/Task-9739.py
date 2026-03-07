from itertools import product

alphabet = 'АГМНСТУ'

ans = []
for word in product('МАНГУСТ', repeat = 6):
    if word[0] != 'У' and word.count('М') == 2 and word.count('Г') <= 1:
        alp_word = ''
        for alp in word:
            alp_word += str(alphabet.index(alp))
        ans.append(int(alp_word, 7))

print(max(ans) + 1)