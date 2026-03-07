from itertools import product

ans = 0

for word in product('ПИТОН', repeat = 4):
    word = ''.join(word)
    key = True
    for a in 'ИО':
        for b in 'ИО':
            if a + b in word:
                key = False
    for a in 'ПТН':
        for b in 'ПТН':
            if a + b in word:
                key = False
    if key:
        ans += 1

print(ans)