def F(x, s):
    if x <= 15:
        return s % 2 == 0
    if s == 0:
        return False
    turns = [F(x - 3, s - 1),
             F(x - 8, s - 1),
             F(x // 3, s - 1)]
    return any(turns) if (s - 1) % 2 == 0 else all(turns)

print('19)', min(*[x for x in range(16, 100) if F(x, 2)]))
print('20)', *[x for x in range(16, 100) if F(x, 3) and not F(x, 1)][:2])
print('21)', min(*[x for x in range(16, 100) if F(x, 4) and not F(x, 2)]))