from string import printable

ans = 0
num = 4**36 + 3*4**20 + 4**15 + 2*4**7 + 49
for let in set(hex(num)):
    if let not in printable[10:36]:
        ans += 1
print(ans)