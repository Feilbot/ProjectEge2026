L = 10 + 52 + 500

amount = 45877
memory = 49 * 1024 * 1024

i = 1
while 2 ** i < L:
    i += 1

print((memory/amount * 8).__ceil__() // i)