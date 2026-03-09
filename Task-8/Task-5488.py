from itertools import product

ans = 0

for word in product('ПОЛИНА', repeat = 8):
    word = "".join(word)
    if sum(word.count(i) for i in 'ПЛН') > sum(word.count(i) for i in 'ОИА'):
        ans += 1
print(ans)