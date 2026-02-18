from string import printable

ans = 0

for x in printable[:25]:

    num = int(f'8AF7{x}11', 25) + int(f'{x}DA97', 25)

    for i in range(1, 101):
        if num % i == 0:
            ans += 1
print(ans)