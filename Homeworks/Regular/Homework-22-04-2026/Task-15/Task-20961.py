from itertools import combinations

def f(x):
    P = 15 <= x <= 142
    Q = 38 <= x <= 167
    A = A1 <= x <= A2
    return not(not(Q <= (((not A) and P) <= (not Q))))

ans = []

line_A = [15, 38, 142, 167]
line_x = [15.5, 38.5, 142.5]

for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)

print(min(ans))