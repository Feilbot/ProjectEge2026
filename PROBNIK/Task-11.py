symbols = 377

amount = 23_155
memory = 5_536 * 1024
i = 1
while 2 ** i < (memory/amount).__ceil__():
    i += 1

print(2 ** i)