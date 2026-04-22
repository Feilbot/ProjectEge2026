from itertools import permutations

ans = 0

for word in permutations('КАЙФ', r = 4):
    word = "".join(word)
    if word[-1] != 'Й' and 'КФ' not in word:
        ans += 1

print(ans)