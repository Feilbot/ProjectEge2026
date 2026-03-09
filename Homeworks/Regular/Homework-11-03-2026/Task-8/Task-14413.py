from itertools import permutations

alphabet = 'СОРТИРОВКА'
gl = set('ОИОА')
sogl = set('СРТРВК')

ans = 0

for word in set(permutations(alphabet)):
    word = "".join(word)
    for i in gl:
        word = word.replace(i, '*')
    for i in sogl:
        word = word.replace(i, '=')
    if '***' not in word and '===' not in word:
        ans += 1

print(ans)