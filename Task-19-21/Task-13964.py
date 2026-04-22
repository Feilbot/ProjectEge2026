def f(x, y, s):
    if x + y <= 108:
        return s % 2 == 0
    if s == 0:
        return False
    turns = [f(x - 2, y, s - 1),
             f((x / 2).__ceil__(), y, s - 1),
             f(x, (y / 2).__ceil__(), s - 1),
             f(x, y - 2, s - 1)]
    return any(turns)

print('19)', max(i for i in range(48 + 1, 100_000) if f(60, i, 2)))

def f(x, y, s):
    if x + y <= 108:
        return s % 2 == 0
    if s == 0:
        return False
    turns = [f(x - 2, y, s - 1),
             f((x / 2).__ceil__(), y, s - 1),
             f(x, (y / 2).__ceil__(), s - 1),
             f(x, y - 2, s - 1)]
    return any(turns) if (s - 1) % 2 == 0 else all(turns)

print('20)', min(i for i in range(48 + 1, 100_000) if f(60, i, 3) and not(f(60, i, 1))), max(i for i in range(48 + 1, 100_000) if f(60, i, 3) and not(f(60, i, 1))))
print('21)', max(i for i in range(48 + 1, 100_000) if f(60, i, 4) and not(f(60, i, 2))))