px = 1024*960
amount = 32
v = 1_474_560
t = 140

# px * 2**i * amount = v * t
# => 2**i = v * t / amount / px

print(2 ** (v * t / amount / px).__floor__())