from string import printable

ans = 0

for x in printable[:22]:
    num = int(f'A23{x}AC0', 22) + int(f'GB{x}21670', 22)
    if num % 21 == 0:
        ans = num // 22
print(ans)