print('x y z w')

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (((y <= (not x)) and y) == w) and z == 1:
                    print(x, y, z, w)

#
#   1   *   0   *
#   *   1   *   *
#   *   0   0   *

# Ответ: zxwy