from itertools import product

# product - создаёт все комбинации определённой длины
# enumerate - нумерует все элементы последовательности

# Task-17549

alphabet = sorted('ФОКУС')

ans = 0

for pos, word in enumerate(product(alphabet, repeat = 5), start = 1):
    word = ''.join(word)
    if 'Ф' not in word and word.count('У') == 2:
        ans = pos
print(ans)

# Task-9739

alphabet = sorted('МАНГУСТ')[::-1]

ans = 0

for pos, word in enumerate(product(alphabet, repeat = 6), start = 1):
    word = ''.join(word)
    if word[0] != 'У' and word.count('М') == 2 and word.count('Г') <= 1:
        ans = pos
print(ans)