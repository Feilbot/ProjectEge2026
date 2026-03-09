from itertools import product

alphabet = sorted('БМЮРН')
ans = 0

for pos, word in enumerate(product(alphabet, repeat = 6), start = 1):
    word = "".join(word)
    if word[0] != 'М' and word.count('Р') >= 2 and 'Ю' not in word and pos % 2 == 1:
        ans = pos

print(ans)