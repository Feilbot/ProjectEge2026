from itertools import product

ans = 0

for word in product('МОЛЬ', repeat = 5):
    word = ''.join(word)
    if 'ОЬ' not in word and word[0] != 'Ь' and 'ЬЬ' not in word:
        ans += 1

print(ans)