from string import printable

for x in printable[:14]:
    num = int(f'4B3{x}1', 14) + int(f'5{x}F83', 16)
    if num % 13 == 0:
        print(num // 13)
        break