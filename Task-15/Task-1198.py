from itertools import combinations

def f(x):
    B = 18 <= x <= 52
    C = 16 <= x <= 41
    A = A1 <= x <= A2
    return (B <= A) and ((not C) or A)

line_A = [16, 18, 41, 52]
line_x = [16.5, 18.5, 41.5]

ans = []

for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)

print(min(ans))