print(bin(172)[2:])
print(bin(16)[2:])
print(len(bin(255)[2:]) * 2 + 2)
print('----')
print(bin(192)[2:])

print(bin(255)[2:])
print('----')
ans = 1
for i in range(8):
    if (len(bin(255)[2:]) * 2 + 2 + i) % 5 != 0:
        ans += 1

print(ans)