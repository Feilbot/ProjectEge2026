from string import printable

for x in printable[:17]:
    num = int(f'4B3{x}1C7', 14) + int(f'5{x}G83F7', 17)
    if num % 15 == 0:
        print(num // 15)
        break