from string import printable

sys = 18

for x in printable[:sys]:
    num = int(f'71{x}264', sys) + int(f'4{x}51{x}1', sys) + int(f'21{x}637', sys)
    if num % 17 == 0:
        print(num // 17)
        break