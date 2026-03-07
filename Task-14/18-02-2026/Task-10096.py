from string import printable

ans = 0

for x in printable[:19]:
    num = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
    if num % 18 == 0:
        ans = num // 18
print(ans)