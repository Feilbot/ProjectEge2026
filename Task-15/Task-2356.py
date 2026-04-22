from itertools import combinations

def f(x):
    P = 10 <= x <= 45
    Q = 35 <= x <= 78
    A = A1 <= x <= A2
    return not (((not P) <= Q) and (not A))

line_A = [10, 35, 45, 78]
line_x = [10.5, 35.5, 45.5]

ans = []

for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)

print(min(ans))