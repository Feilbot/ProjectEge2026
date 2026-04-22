def f(x, s):
    if x <= 30:
        return s % 2 == 0
    if s == 0:
        return False
    turns = [f(x - 3, s - 1),
             f(x - 5, s - 1),
             f(x // 4, s - 1)]
    return any(turns) if (s - 1) % 2 == 0 else all(turns)

print('19)', [i for i in range(31, 1000) if f(i, 2)][0])
print('20)', *[i for i in range(31, 1000) if f(i, 3) and not f(i, 1)][:2])
print('21)', [i for i in range(31, 1000) if f(i, 4) and not f(i, 2)][0])