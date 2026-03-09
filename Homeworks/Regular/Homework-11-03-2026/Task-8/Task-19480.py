from itertools import permutations

ans = 0

for word in set(permutations('ПАРИЖАНКА')):
    word = "".join(word)
    if word.count('АА') + word.count('АИ') + word.count('ИА') == 1 and 'ААА' not in word:
        ans += 1

print(ans)