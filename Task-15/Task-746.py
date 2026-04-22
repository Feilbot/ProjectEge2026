from itertools import combinations

def f(x):
    P = 12 <= x <= 26
    Q = 30 <= x <= 53
    A = A1 <= x <= A2
    return (A <= P) or Q

line_A = [12, 30, 26, 53]
line_x = [12.5, 30.5, 26.5]

ans = []

for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)

print(max(ans))