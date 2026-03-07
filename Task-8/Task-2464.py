'''from itertools import product

ans = 0

for word in product('НИЧЬЯ', repeat = 7):
    word = ''.join(word)
    if word.count('И') + word.count('Я') == 2 and 'ЯИ' not in word and 'ИЯ' not in word and 'ИИ' not in word and 'ЯЯ' not in word:
        ans += 1

print(ans)'''

from itertools import product

ans = 0

for word in product('НИЧЬЯ', repeat = 7):
    word = ''.join(word)
    if word.count('И') + word.count('Я') == 2:
        key = True
        for a in 'ИЯ':
            for b in 'ИЯ':
                if a + b in word:
                    key = False
        if key:
            ans += 1

print(ans)