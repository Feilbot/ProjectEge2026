from string import printable

ans = 0

for x in printable[:25]:
    num = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if num % 24 == 0:
        ans = num // 24
print(ans)