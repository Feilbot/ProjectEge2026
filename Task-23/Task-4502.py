def f(x, y, cnt):
    if x > y or cnt > 6:
        return 0
    elif x == y:
        if cnt == 6:
            return 1
        else:
            return 0
    else:
        return f(x + 1, y, cnt+1) + f(x + 2, y, cnt+1) + f(x * 2, y, cnt+1)

ans = 0

for x in range(34, 60):
    if f(1, x, 0):
        ans += 1

print(ans)