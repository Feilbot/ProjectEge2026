from itertools import combinations

def f(x):
    P = 5 <= x <= 30
    Q = 14 <= x <= 23
    A = A1 <= x <= A2
    return (P == Q) <= (not A)

line_A = [5, 14, 23, 30]
line_x = [5.5, 14.5, 23.5]

ans = []

for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)

print(max(ans))