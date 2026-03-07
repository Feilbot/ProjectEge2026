from itertools import product

ans = 0

for word in product('ПСКАЛЬ', repeat = 4):
    word = ''.join(word)
    if word[0] != 'Ь' and 'ЬЬ' not in word:
        ans += 1

print(ans)