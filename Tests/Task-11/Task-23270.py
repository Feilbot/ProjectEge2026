alphabet = 10 + 27
kolvo = 3548
mem = 12 * 1024 * 8

# i = int(input())
# while 2 ** i < alphabet:
#     i = int(input())

# => i = 6

print((mem / kolvo / 6).__ceil__())
