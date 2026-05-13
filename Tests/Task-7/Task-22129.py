size = 2560 * 1440
group = 52
v = 8388608
t = 520
i = 1
while size * i * group / v < t:
    i += 1

print(2**(i - 1) + 1)