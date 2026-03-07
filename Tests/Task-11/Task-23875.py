alphabet = 10 + 52 + 50
i = 1
while 2**i < alphabet:
    i += 1

amount = 800177
size = 35 * 1024 * 1024 * 8
print((size/amount/i).__floor__())