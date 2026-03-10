print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if (y <= x) and (not z and w):
                    print(x, y, z, w)
print('Ответ: wxyz')