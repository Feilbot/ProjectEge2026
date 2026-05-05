colors = 10_000_000
packs = 10
v = 2_100_000
time = 3 * 60

i = 1
while 2 ** i < colors:
    i += 1

# V = h * w * i
print(v * time / i / packs)