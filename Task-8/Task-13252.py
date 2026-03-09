from itertools import permutations

ans = 0

for word in set(permutations('КИДАЛА', 5)):
    word = "".join(word)
    if 'АА' not in word:
        ans += 1

print(ans)