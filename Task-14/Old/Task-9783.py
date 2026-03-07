from string import printable

for x in printable[:22]:
    num = int(f'18{x}89957', 22) + int(f'80{x}33', 22) + int(f'521{x}6', 22)
    if num % 21 == 0:
        print(num // 21)
        break