from string import printable

ans = 0

for x in printable[:19]:
    num = int(f'98{x}79641', 19) + int(f'36{x}14', 19) + int(f'73{x}4', 19)
    if num % 18 == 0:
        ans = num // 18
print(ans)