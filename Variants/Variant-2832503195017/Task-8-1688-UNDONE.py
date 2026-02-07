from itertools import product

sogl = 'КСН'
glas = 'ЕИЯ'
for LEN in range(2, 7):
    for i in product('КСЕНИЯ', repeat = LEN):
        print(i)