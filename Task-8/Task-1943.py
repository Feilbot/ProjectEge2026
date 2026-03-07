from itertools import product

ans = 0

for word in product('ЗЕРКАЛО', repeat = 6):
    word = ''.join(word)
    if 1 <= word.count('К') <= 4 and len(set(word)) + word.count('К') - 1 == len(word):
        ans += 1

print(ans)