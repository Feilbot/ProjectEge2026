from itertools import product

alphabet = sorted('ШКОЛА')

for pos, word in enumerate(product(alphabet, repeat = 5), start=1):
    word = "".join(word)
    if word == 'ШАЛАШ':
        print(pos)
        break