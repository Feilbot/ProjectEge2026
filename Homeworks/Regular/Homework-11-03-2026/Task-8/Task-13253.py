from itertools import product

ans = 0

library = []

for word_1 in product('КОНЕЦ', repeat = 5):
    library.append("".join(word_1))

for word_2 in product('ДРАКОН', repeat = 5):
    library.append("".join(word_2))

for word in library:
    if library.count(word) == 1:
        ans += 1

print(ans)