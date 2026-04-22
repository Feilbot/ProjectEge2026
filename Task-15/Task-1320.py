from itertools import combinations

def f(x):
    P = 12 <= x <= 28
    Q = 15 <= x <= 30
    A = A1 <= x <= A2
    return (P <= A) and ((not Q) or A)

line_A = [12, 15, 28, 30]
line_x = [12.5, 15.5, 28.5]

ans = []

for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)

print(min(ans))