from itertools import combinations

def f(x):
    P = x in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    Q = x in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    R = x in [12, 24, 36, 48, 60]
    A = x in [A1, A2]
    return (not A) <= ((P and Q) <= R)

ans = []

line = sorted([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 12, 24, 36, 48, 60])

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A1 * A2)

print(min(ans))