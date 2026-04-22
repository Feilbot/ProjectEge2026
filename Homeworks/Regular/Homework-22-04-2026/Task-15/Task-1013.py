from itertools import combinations

def f(x):
    P = 23 <= x < 45
    Q = 34 <= x <= 56
    A = A1 <= x <= A2
    return (not A) or (not P) and Q

ans = []

line_A = [23, 34, 45, 56]
line_x = [23.5, 34.5, 45]

for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)

print(max(ans))