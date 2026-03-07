from itertools import product

answer = 0

for x in range(5, 8):
    for word in product('БЕРСК', repeat = x):
        answer += 1

print(answer)