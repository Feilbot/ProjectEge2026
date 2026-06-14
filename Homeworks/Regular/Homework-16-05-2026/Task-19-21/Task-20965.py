def f(x, y, s):
    if x <= y: return s % 2 == 0
    if s == 0: return False
    h = [
        f(x - 2, y, s - 1),
        f(x * 2 // 3, y, s - 1)
    ]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', [i for i in range(14, 200) if f(i, 13, 2)][0])
print('20)', *[i for i in range(14, 200) if f(i, 13, 3) and not f(i, 13, 1)][:2])
print('21)', [i for i in range(14, 200) if (f(i, 13, 2) or f(i, 13, 4)) and not f(i, 13, 2)][0])