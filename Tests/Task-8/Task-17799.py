from itertools import product

ans = 0

for pos, word in enumerate(product(sorted('АРГУМЕНТ'), repeat = 4), start=1):
    word = "".join(word)
    if len(word) == len(set(word)) and word == "".join(sorted(word)):
        ans = pos

print(ans)