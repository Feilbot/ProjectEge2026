num = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024

ans = 0

while num:
    if num % 25 == 0:
        ans += 1
    num //= 25

print(ans)