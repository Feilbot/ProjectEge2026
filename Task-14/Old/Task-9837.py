from string import printable

sys = 23

for x in printable[:sys]:
    num = int(f'7{x}38596', sys) + int(f'14{x}36', sys) + int(f'61{x}7', sys)
    if num % 22 == 0:
        print(num // 22)
        break