def F(x, s):
    if x >= 111:
        return s % 2 == 0
    if s == 0:
        return False
    tunrs = [F(x + 3, s - 1),
             F(x + 1, s - 1),
             F(x * 4, s - 1)]
    return any(tunrs) if (s - 1) % 2 == 0 else all(tunrs)

print('19)', *[x for x in range(1, 111) if F(x, 2)])
print('20)', *[x for x in range(1, 111) if F(x, 3) and not F(x, 1)])
print('21)', min(*[x for x in range(1, 111) if F(x, 4) and not F(x, 2)]))