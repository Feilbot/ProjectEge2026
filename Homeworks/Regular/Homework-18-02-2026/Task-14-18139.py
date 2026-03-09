from string import printable

ans = 0

for y in range(1, 101):
    for x in printable[1:25]:

        num = int(f'8AF7{x}11', 25) + int(f'{x}DA87', 25)

        if num % y == 0:
            ans += 1
            break
print(ans)