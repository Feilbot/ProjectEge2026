from itertools import combinations

def f(x):
    D = 17 <= x <= 58
    C = 29 <= x <= 80
    A = A1 <= x <= A2
    return D <= (((not C) and (not A)) <= (not D))

line_A = [17, 29, 58, 80]
line_x = [17.5, 29.5, 58.5]

ans = []

for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)

print(min(ans))