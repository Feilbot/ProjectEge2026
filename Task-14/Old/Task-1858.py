num = 4 * 625**9 - 25**15 + 2 * 5**11 - 7
cnt = 0
while num :
    if num % 5 == 4:
        cnt += 1
    num //= 5
print(cnt)